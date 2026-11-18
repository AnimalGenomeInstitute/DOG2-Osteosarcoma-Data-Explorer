# Canine Osteosarcoma (DOG2): ICDC Clinical and Expression Crosswalk

**Data release candidate — 18 November 2026**  
Curated, dog-level crosswalk from an ICDC file manifest and public GEO / publication supplementary datasets.

## What is included?

| File | Rows | Fields | Description |
| --- | ---: | ---: | --- |
| [`data/Case_Summary_303.csv`](data/Case_Summary_303.csv) | 303 | 53 | Clinical outcome summary, demographics, source provenance, assay availability, tissue information, and GEO IDs |
| [`data/Case_Expression_303.csv`](data/Case_Expression_303.csv) | 303 | 32 | Expression data availability by dog: RNA-seq, NanoString, tissue/sample summaries, PBMC publication evidence, and GEO IDs |

The two tables use the same **`Case ID`** and have one row per unique dog. `Case_Summary_303.csv` uses **`Study Code`**; `Case_Expression_303.csv` uses **`Study`**. This is **not** an expression-count matrix or a repository for FASTQ/RCC files.

## Coverage

| Study | Dogs |
| --- | ---: |
| COTC021 | 105 |
| COTC022 | 102 |
| COTC026 | 70 |
| COTC030 | 26 |
| **Total** | **303** |

- Numeric overall survival (OS) **and** DFS/DFI: **288 dogs**
- Numeric DFS/DFI but not numeric OS follow-up: **5 dogs**
- Neither numeric interval found in the reviewed tables: **10 dogs**
- RNA-seq files recorded in the supplied ICDC manifest: **280 dogs** (280 primary-tumor samples)
- NanoString RCC files recorded in the supplied ICDC manifest: **40 dogs** (115 samples: 23 primary, 92 metastatic)
- PBMC scRNA-seq dog IDs confirmed from a publication: **2 dogs** (`COTC030-1007`, `COTC030-1024`)

The ICDC manifest snapshot contains **no PBMC expression files**; this does **not** mean PBMC profiling was not performed.

## How to join

Use `Case ID` in both files (not GEO GSM). A dog may have several GSM accessions:
- `RNAseq_GSMs`: tumor RNA-seq accessions
- `NanoString_GSMs`: NanoString accessions
- `GEO_GSEs`: associated GEO series

Multiple GSMs in one cell are separated by `; `. A GSM is a **GEO sample accession**, not a FASTQ filename.

## Interpretation and limitations

1. **Data availability is snapshot-based.** `YES` indicates a relevant file/sample in the *supplied* ICDC manifest, not successful local download. `NO` or `NOT_LISTED` does not prove the assay was never performed.
2. **Outcomes were gathered from heterogeneous sources.** The original labels **DFS** and **DFI** are retained; their start dates and endpoint definitions should be harmonized before pooled survival analysis.
3. **Event/censor codes are not fully harmonized.** Fields ending `_RAW` or `_original` preserve source values; do not treat them as a validated universal event indicator.
4. **Not all follow-up is complete.** Five COTC030 dogs have an `Alive` entry without numeric OS follow-up; two have neither interval. Eight COTC026 dogs lack the reviewed outcomes.
5. **Sample identity exceptions are flagged, not resolved.** `COTC021-0201` has a proposed NanoString sample-title alias requiring verification; `COTC021-1913` has an ICDC RCC record without a matched GSM; `COTC022-0618` has a GEO RNA-seq sample not found in the manifest snapshot.
6. **PBMC evidence is separate from file access.** A published scRNA-seq analysis is confirmed for `COTC030-1007` (long DFI) and `COTC030-1024` (short DFI). Their PBMC scRNA-seq files are not in the supplied ICDC manifest. Other dogs are `NOT_ID_VERIFIED`, not definitively negative.
7. **COTC021/COTC022 rows overlap across transcriptomic assays.** Counts of unique dogs must not be inferred from the total number of GSM accessions or ICDC file rows.
8. These tables are **research metadata, not a clinical prediction model** or proof of biologic causality.

## Data sources

- [NCI Integrated Canine Data Commons](https://caninecommons.cancer.gov/) — uploaded ICDC file-manifest snapshot
- [GSE238110](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE238110) — tumor bulk RNA-seq (COTC021/022)
- [GSE313593](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313593) — primary / metastatic tumor NanoString
- [GSE318201](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318201) — COTC026 pretreatment tumor RNA-seq
- [GSE304066](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304066) — COTC030 pretreatment tumor RNA-seq
- [COTC021/022 immune subtype and clinical outcome study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11647208/) — supplementary data
- [Silver et al., COTC021/022 necropsy study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10842475/) — supplemental individual dog outcomes
- [2026 integrated multiomic osteosarcoma study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13430567/) — Supplementary Table S2
- [COTC030 IL-15 study](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1672790/full) — PBMC scRNA-seq publication evidence

See [data dictionary](docs/DATA_DICTIONARY.md) and [publication checklist](docs/PUBLICATION_CHECKLIST.md).

## Release and reuse

Prepared as a GitHub-ready export of the uploaded workbook's two worksheets, without altering their outcome/availability values. Before making a **public** GitHub repository, verify the original data-source redistribution terms and organizational approval. No independent license for third-party source data is claimed by this repository.

The data describe canine research specimens and exclude owner-level identifying fields in these two exported sheets.
