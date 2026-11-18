# Pre-publication checklist

Before pushing the tables to a **public** repository:

- [ ] Confirm that the ICDC manifest and clinical information may be redistributed as a derived crosswalk under the applicable terms.
- [ ] Confirm institutional/project approval to release the integrated individual-animal clinical metadata and source mapping.
- [ ] Verify individual-level clinical outcome values and audit flags against the original supplemental tables.
- [ ] Leave **DFS** and **DFI** distinct until definitions and time origins have been harmonized.
- [ ] Confirm the meaning of `OS_status_S10_original`, `DFS_status_S10_original`, and 2026 `_RAW` censor fields before analysis.
- [ ] Document the sample-name alias and other GEO–ICDC exceptions; do not silently force-match IDs.
- [ ] Confirm that PBMC assay evidence is not misrepresented as openly accessible sequencing data.
- [ ] Decide the appropriate license only for original contributions; do not assume third-party data can be relicensed.
- [ ] Optionally include a methods description, release version, and contact in the repository.

Suggested commit message: `Add DOG2 ICDC dog-level clinical and expression crosswalk (303 cases)`

**Upload:** In an existing GitHub repository, choose **Add file → Upload files** and add the files from `data/`, `docs/`, `scripts/`, plus `README.md`. Keep these paths so the README links work. Alternatively, copy the project folder into a local clone and commit/push.
