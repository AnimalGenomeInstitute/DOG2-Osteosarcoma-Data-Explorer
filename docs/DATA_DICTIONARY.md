# Data dictionary

Original column names are preserved from the uploaded Excel sheets. This is a field interpretation guide, not a new harmonization.

## Selected fields

| Field | Description |
| --- | --- |
| `Study Code` | Clinical trial code (COTC021, COTC022, COTC026, or COTC030). |
| `Case ID` | Unique canine study-specific ID; join key. |
| `Clinical_Outcome_Status` | Completeness category for numeric OS and DFS/DFI intervals; event flags not necessarily validated. |
| `OS_days` | Overall survival interval in days, as recorded in the source. |
| `DFS_DFI_days` | Disease-free survival or interval in days; original endpoint must be checked. |
| `DFS_DFI_endpoint_original` | Original source's label (DFS or DFI). |
| `OS_status_S10_original` | Raw 0/1 original OS status from Supplementary Table S10. |
| `DFS_status_S10_original` | Raw 0/1 original DFS status from Supplementary Table S10. |
| `Survival_censor_2026_RAW` | Unmodified code from 2026 source, not harmonized. |
| `DFI_censor_2026_RAW` | Unmodified code from 2026 source, not harmonized. |
| `OS_raw_value_2026` | Original OS field, including text such as `Alive`. |
| `Clinical_Treatment` | Study-reported treatment description or arm. |
| `Outcome_Source` | Human-readable reference for clinical outcomes. |
| `Outcome_Source_URL` | URL for primary clinical outcome source. |
| `Outcome_Source_Secondary` | Optional secondary source for cross-reference. |
| `Reason_off_study_Silver` | Text status from Silver et al. source. |
| `RNAseq_in_ICDC_Manifest` | YES if at least one RNA-seq sample is listed in the supplied ICDC manifest. |
| `NanoString_in_ICDC_Manifest` | YES if at least one NanoString sample is listed in the supplied ICDC manifest. |
| `PBMC_scRNAseq_Published_Status` | Publication-confirmed dog ID versus not verified; NOT an assay absence flag. |
| `PBMC_Files_in_ICDC_Manifest` | Whether PBMC assay files were listed in supplied ICDC manifest (NOT_LISTED in this snapshot). |
| `GEO_GSEs` | Semicolon-delimited series IDs. |
| `RNAseq_GSMs` | Semicolon-delimited GEO accessions for bulk RNA-seq. |
| `NanoString_GSMs` | Semicolon-delimited GEO accessions for NanoString. |
| `GEO_match_status` | Status of matching ICDC and GEO sample identifiers. |
| `GEO_match_notes` | Human-readable matching evidence or exceptions. |
| `Study` | Clinical trial code; equivalent to `Study Code` in the summary. |
| `Clinical outcome status` | Same completeness category in expression table. |
| `OS days` | Overall survival interval in days, as recorded in the source. |
| `DFS/DFI days` | Disease-free survival or interval in days; not necessarily harmonized. |

## Column inventory

### `Case_Summary_303.csv` (53 columns)

```text
Study Code, Case ID, Clinical_Outcome_Status, OS_days, DFS_DFI_days, DFS_DFI_endpoint_original, OS_status_S10_original, DFS_status_S10_original, Survival_censor_2026_RAW, DFI_censor_2026_RAW, OS_raw_value_2026, Clinical_Treatment, Outcome_Source, Outcome_Source_URL, Outcome_Source_Secondary, Reason_off_study_Silver, ICDC_File_Count, ICDC_Unique_Samples, ICDC_RNAseq_File_Count, ICDC_NanoString_File_Count, Representative_Sample_ID, ICDC_Breed, ICDC_Age_years, ICDC_Follow_Up_Data, Clinical_ID_Match, Clinical_QC_Notes, RNAseq_in_ICDC_Manifest, RNAseq_Unique_Samples, RNAseq_Primary_Samples, RNAseq_Metastasis_Samples, RNAseq_Blood_Samples, NanoString_in_ICDC_Manifest, NanoString_Unique_Samples, NanoString_Primary_Samples, NanoString_Metastasis_Samples, NanoString_Blood_Samples, Expression_Assay_Mix, Expression_Tissue_Summary, Expression_Sample_Sites, NanoString_GEO_Title_QC, PBMC_scRNAseq_Published_Status, PBMC_Assay_Confirmed, PBMC_Files_in_ICDC_Manifest, PBMC_Prognosis_Group, PBMC_Publication_URL, PBMC_Evidence_Notes, GEO_GSEs, RNAseq_GSMs, NanoString_GSMs, GEO_nonexact_GSMs, GEO_GSM_count, GEO_match_status, GEO_match_notes
```

### `Case_Expression_303.csv` (32 columns)

```text
Study, Case ID, Clinical outcome status, OS days, DFS/DFI days, RNAseq_in_ICDC_Manifest, RNAseq_Unique_Samples, RNAseq_Primary_Samples, RNAseq_Metastasis_Samples, RNAseq_Blood_Samples, NanoString_in_ICDC_Manifest, NanoString_Unique_Samples, NanoString_Primary_Samples, NanoString_Metastasis_Samples, NanoString_Blood_Samples, Expression_Assay_Mix, Expression_Tissue_Summary, Expression_Sample_Sites, NanoString_GEO_Title_QC, PBMC_scRNAseq_Published_Status, PBMC_Assay_Confirmed, PBMC_Files_in_ICDC_Manifest, PBMC_Prognosis_Group, PBMC_Publication_URL, PBMC_Evidence_Notes, GEO_GSEs, RNAseq_GSMs, NanoString_GSMs, GEO_nonexact_GSMs, GEO_GSM_count, GEO_match_status, GEO_match_notes
```

Empty cells indicate that the relevant field was not populated in the workbook; they should not be interpreted as zero, absence of disease, or no assay.
