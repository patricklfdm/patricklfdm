# Profile visual design

The visual identity represents Patrick Li personally; decorative labels must not imply an affiliated laboratory or institution.

## Visual system

| Role | Color |
| --- | --- |
| Background | `#0B1220` |
| Surface | `#152337` |
| Cyan accent | `#7DD3FC` |
| Green accent | `#34D399` |
| Primary text | `#F8FAFC` |
| Secondary text | `#B6C6D9` |

The SVG surfaces keep the same appearance in light and dark themes; native Markdown inherits GitHub's theme. Arial/Helvetica/system sans-serif avoids font downloads. Topology motifs are decorative; the GSE architecture explicitly identifies itself as conceptual.

## Asset inventory

| Asset | Placement | Purpose |
| --- | --- | --- |
| [hero.svg](../assets/hero.svg) | Profile header | Identity and distributed-node motif |
| [gse-card.svg](../assets/gse-card.svg) | Flagship section | Public engineering focus |
| [wayvia-card.svg](../assets/wayvia-card.svg) | Private engineering section | AI product engineering |
| [gse-architecture.svg](../assets/gse-architecture.svg) | GSE showcase | Conceptual system layers |

Core descriptions remain native text. Cards use short labels; fine decorative labels are supplementary on mobile. The architecture has an equivalent prose explanation. Additional research/stack cards were intentionally omitted to keep the profile concise.

## Maintenance

Edit text directly in Markdown. Edit the SVG generator rather than hand-editing its generated outputs:

```sh
python3 scripts/generate_assets.py
python3 scripts/validate_assets.py
```

Commit both the generator and generated SVGs. CI validates local references and SVG XML/accessibility metadata, rejects active or remote SVG content, and checks deterministic regeneration. It needs no secrets and retrieves no private repository content. Review actual rendering separately; structural checks do not prove visual correctness. The Markdown checker supports this repository's inline, explicit reference-style, and HTML references; it is not a general CommonMark parser and does not validate heading fragments or remote availability.

Recheck GSE release status when updating claims. Keep owner-supplied private-project descriptions high-level, with no private source links or internal assets. New screenshots require explicit publication approval.

## Native private contributions

On GitHub, open **Your profile**, choose **Contribution settings** above the contribution calendar, then enable **Private contributions**. This shows anonymized private activity, not private repository details. This is a manual account preference; this project does not change it or collect private activity.

Source: [GitHub's visibility instructions](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/manage-visibility-settings-for-private-contributions-and-achievements?apiVersion=2022-11-28).

## Publication

The target is the public profile repository `patricklfdm/patricklfdm`, with README.md at its root. Local preparation does not authorize remote creation or a push. Use the [publication review](PUBLICATION_REVIEW.md) before publication.
