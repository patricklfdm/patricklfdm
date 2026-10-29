# Patrick Li profile — consolidated implementation brief

## Objective

Build the public-facing contents of `patricklfdm/patricklfdm`, with a root README that communicates Patrick's engineering identity within 15 seconds. GSE is the flagship; Wayvia connects systems engineering to AI products; research directions describe future interests. Write profile content in English.

## Content hierarchy

1. Hero: Patrick Li; Engineering Systems That Scale.; research engineering identity.
2. About: concise focus statement, resume-supported current/prior roles, and CMU/UCI education.
3. General Search Engine: resume-aligned engineering achievements and scoped evaluation figures, per the owner's subsequent instruction; retain release-specific references in the showcase.
4. Private engineering: Wayvia's user-provided high-level description only.
5. Research: two planned directions; no implied publications or results.
6. Technology: four compact native-text groups.
7. Activity: native GitHub profile navigation; no metrics service.
8. Contact: user-provided GitHub, LinkedIn, and email.

Keep the root README concise and scannable. Move supporting detail to showcase pages. Do not generate decorative assets solely to satisfy an example directory structure. Omit additional private projects until sufficient approved public descriptions exist.

## Visual contract

Dark navy palette: background #0B1220, surface #152337, cyan #7DD3FC, green #34D399, text #F8FAFC. Minimal architectural composition and distributed-node motifs. Use native Markdown for readable, selectable core content. SVGs control their own surfaces, not the GitHub page background. No JavaScript, external fonts, animation, remote badges, or unsupported HTML/CSS in the README.

Create three primary visual assets: hero, GSE card, Wayvia card. Place the conceptual GSE architecture in its supporting page. Give each SVG a viewBox, opaque background, accessible title/description, and readable typography. Keep paths relative and assets in version control.

## Evidence and privacy

Use the updated resume as the requested editorial source for GSE achievements. Distinguish owner-reported figures from independently checked public evidence. Do not imply that all implementation work belongs to a single published release; retain release-specific source links and scope the architecture diagram to v5.1. Do not infer performance or reliability guarantees from test existence. Education, professional identity, and stack labels are supported by the user-supplied resume. Use only supplied high-level Wayvia descriptions; do not inspect private repositories for material. Keep the resume PDF as an ignored local reference; do not publish its phone number or automatically add a download link. Omit private URLs, repository metadata, screenshots, internal diagrams, and implementation details. Research defaults to planned unless ongoing status is confirmed.

## Delivery and validation

Deliver README, showcase pages, SVG sources, reproducible asset generation, a dependency-free local validator, and least-privilege CI. Check local references and SVG safety automatically. Render and inspect light/dark desktop and mobile previews separately. Check public URLs; record access restrictions as unverified rather than broken. Maintain a concise publication review with manual claims and validation limits.

Implement locally. Do not create a remote repository, push, publish, or change account settings without explicit authorization. Do not modify other project repositories.
