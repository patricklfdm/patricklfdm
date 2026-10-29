# Publication review

Review date: October 29, 2026 (America/Los_Angeles). Local draft; not pushed or published.

## Evidence and claim boundaries

| Claim | Evidence / status |
| --- | --- |
| Java 21, typed filtering, full-text retrieval, BM25 | Public GSE README, pom.xml, and RankedSearcher.java inspected |
| WAL, checkpoints, recovery, immutable snapshots | Public README and durable API inspected; GSE tests were not rerun for this profile task |
| Automatic election, quorum publication, strong leader reads | Public v5.1 migration guide; fixed three-voter group explicitly stated |
| Strong / stale-allowed / minimum-progress reads | Resume-aligned implementation summary; previously inspected public evidence places these in v5.2 development, not the v5.1 release |
| Evaluation and reproducible delivery | Public evidence supports qualification work; 2.50 ms P50 / 5.26 ms P99, 4K documents, three-node GCP, and 61 scenario executions are owner-reported resume figures, not independently rerun |
| Education and Research Engineer identity | Cross-checked against user-supplied resume: CMU M.S. 2025, UCI B.S. 2023; Research Engineer at Pacific Sports Promotion Association |
| Wayvia description and stack | User-supplied resume supports role, dates, AI workflow, vector search, application stack, and operations; no private repositories inspected |
| Research directions | User-provided topics, conservatively labeled planned; no results claimed |
| Technology stack | Aligned with explicit skills in the updated resume, including TypeScript and SQL; all displayed languages, frameworks, messaging, cloud, and observability tools are resume-supported |

Public evidence links are retained below for maintenance rather than displayed on the showcase. Additional code checks: [RankedSearcher.java](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/src/main/java/io/github/patricklfdm/generalsearch/ranking/RankedSearcher.java) and [DurableSearchEngine.java](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/src/main/java/io/github/patricklfdm/generalsearch/durability/DurableSearchEngine.java).

## Link review

- GitHub profile: public page accessible through web tooling.
- GSE repository: GitHub connector confirms public visibility.
- All six linked GSE files: successfully read through the GitHub connector.
- GitHub private-contribution instructions: available through official documentation search.
- LinkedIn: access returned status 999; URL retained as supplied, manual verification required.
- Email and LinkedIn address: match the resume; mailbox delivery and LinkedIn accessibility remain unverified. No verification message sent.
- No Wayvia product URL supplied or invented. No private repository navigation links included.

## Validation

See the final local validation summary below. Preview CSS approximates GitHub Markdown; it is not a hosted GitHub rendering guarantee. CI is prepared but has not run on GitHub. Public-repository evidence was inspected, not independently reproduced.

## Before publication

- [x] Cross-check education, professional title, contact address, and technology labels against the supplied resume.
- [ ] Approve Wayvia's supplied high-level description for public display.
- [ ] Confirm that research should remain labeled planned.
- [ ] Open LinkedIn manually and confirm the profile destination.
- [ ] Recheck version-sensitive GSE statements if publication happens later.
- [ ] Authorize creation/update of `patricklfdm/patricklfdm` and push.
- [ ] After publication, inspect actual GitHub desktop/mobile rendering and CI status.

No additional private projects, private metadata, screenshots, internal diagrams, credentials, or private implementation materials were copied into this repository.

## Final local validation summary

- PASS: 20 local references and four SVG assets; XML, accessibility metadata, and self-contained resource checks.
- PASS: regenerating all four assets produces identical SHA-256 hashes.
- PASS: validator accepts a valid fixture and rejects a missing local target, malformed SVG, and embedded script.
- PASS: Chromium previews at 375, 390, and 1000 CSS pixels in both light and dark themes; all images load and no horizontal overflow is detected.
- Visual inspection: desktop dark profile, mobile light/dark profile, and standalone architecture diagram. Small card labels remain supplementary; important content is repeated as native text.
- Limit: these are local Markdown previews, not screenshots of a published GitHub profile.

The workspace exposes a read-only `.git` placeholder. Local Git metadata is therefore stored separately under `/tmp`; a complete Git bundle is saved in the ignored `.preview` directory as a portable backup. Public source files remain at the workspace root. No remote is configured.

## Resume reconciliation

The user-supplied resume was reviewed on October 29, 2026. It supports the full name, current research engineering role, previous Wayvia role, graduation years, and the revised technology groups. The PDF remains a local, ignored reference; its telephone number is not included in the public profile.

The resume's GSE wording includes “safe membership transitions.” The previously inspected public v5.1 guide explicitly excludes dynamic membership. At the owner's subsequent explicit request, the profile uses the resume's membership-transition wording. This is not independent verification of dynamic membership support; the architecture diagram remains specifically scoped to public v5.1.

Following the owner's instruction to use the resume for GSE, GSE latency/scenario figures are now included with the reported setup. At the owner's request, source attribution is retained only in maintenance documentation. They have not been independently reproduced. The architecture illustration remains scoped to v5.1. Wayvia completion-rate figures remain omitted. Research status is not established by the resume and stays planned. Additional experience and DinnerMate were not expanded into new cards, preserving the GSE/Wayvia focus.

## Maintenance evidence links

- [Project overview and retrieval examples](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/README.md)
- [Java 21 build configuration](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/pom.xml)
- [v5.1 operating modes and migration boundaries](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/docs/v5x/v5.1/MIGRATION_GUIDE.md)
- [v5.2 local qualification record](https://github.com/patricklfdm/GeneralSearchEngine/blob/master/docs/v5x/v5.2/PHASE_4_QUALIFICATION.md)

Source attribution and verification commentary are intentionally omitted from the profile and showcase presentation at the owner's request. This does not change the evidence status recorded above. Public/private source-code availability labels and project navigation remain part of the presentation.
