#!/usr/bin/env python3
"""Offline checks for this repository's Markdown, HTML references and SVG assets.

Supports inline/reference Markdown links and HTML src/href attributes. Deliberately
skips fenced code. Does not claim to validate remote links or visual rendering.
"""
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SVG = '{http://www.w3.org/2000/svg}'
errors = []
count = 0

def fail(path, message):
    errors.append(f'{path.relative_to(ROOT)}: {message}')

def check_ref(source, reference):
    global count
    parsed = urlsplit(reference)
    if parsed.scheme in {'https', 'http', 'mailto'}:
        return
    if parsed.scheme or parsed.netloc:
        fail(source, f'unsupported reference: {reference}')
        return
    if not parsed.path:
        return
    count += 1
    target = (source.parent / unquote(parsed.path)).resolve()
    if not target.is_relative_to(ROOT) or parsed.path.startswith('/'):
        fail(source, f'non-relative/out-of-repository reference: {reference}')
    elif not target.exists():
        fail(source, f'missing reference: {reference}')

class References(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'href'):
            if key in attrs:
                check_ref(self.source, attrs[key])
        if tag == 'img' and not attrs.get('alt'):
            fail(self.source, 'image requires alt text')

for path in sorted(ROOT.rglob('*.md')):
    if any(p.startswith('.') for p in path.relative_to(ROOT).parts):
        continue
    content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
    definitions = dict(re.findall(r'^\s*\[([^\]]+)\]:\s*<?([^\s>]+)>?', content, re.M))
    for reference in definitions.values():
        check_ref(path, reference)
    for match in re.finditer(r'!?\[([^\]\n]*)\]\(<?([^\s)>]+)>?(?:\s+"[^"]*")?\)', content):
        check_ref(path, match[2])
        if match[0].startswith('!') and not match[1].strip():
            fail(path, 'image requires alt text')
    for label, key in re.findall(r'\[([^\]\n]+)\]\[([^\]\n]*)\]', content):
        if (key or label) not in definitions:
            fail(path, f'undefined reference link: {key or label}')
    References(path).feed(content)

assets = sorted((ROOT / 'assets').glob('*.svg'))
if not assets:
    errors.append('No SVG assets found.')
for path in assets:
    raw = path.read_text()
    if re.search(r'<!DOCTYPE|<!ENTITY', raw, re.I):
        fail(path, 'DTD/entities are forbidden')
        continue
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        fail(path, f'malformed SVG: {exc}')
        continue
    if root.tag != SVG + 'svg':
        fail(path, 'invalid SVG root or namespace')
    try:
        box = [float(x) for x in root.attrib['viewBox'].split()]
        assert len(box) == 4 and box[2] > 0 and box[3] > 0
    except (KeyError, ValueError, AssertionError):
        fail(path, 'missing or invalid viewBox')
    for tag in ('title', 'desc'):
        element = root.find(SVG + tag)
        if element is None or not (element.text or '').strip():
            fail(path, f'missing accessible {tag}')
    ids = [el.attrib['id'] for el in root.iter() if 'id' in el.attrib]
    if len(ids) != len(set(ids)):
        fail(path, 'duplicate SVG IDs')
    for el in root.iter():
        tag = el.tag.rsplit('}', 1)[-1]
        if tag in {'script', 'foreignObject', 'image', 'animate', 'animateTransform', 'set', 'style'}:
            fail(path, f'unsupported active/external element: {tag}')
        for key, value in el.attrib.items():
            key = key.rsplit('}', 1)[-1]
            if key.lower().startswith('on') or key == 'style':
                fail(path, f'unsafe attribute: {key}')
            if key == 'href' and not value.startswith('#'):
                fail(path, 'SVG must be self-contained')
            for ref in re.findall(r'url\(([^)]+)\)', value):
                if not ref.startswith('#') or ref[1:] not in ids:
                    fail(path, f'invalid SVG resource: {ref}')
            if key == 'href' and value.startswith('#') and value[1:] not in ids:
                fail(path, f'missing SVG target: {value}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {count} local references; {len(assets)} SVG files; XML, accessibility metadata, and self-contained SVG checks.')
