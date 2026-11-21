
# Reproducibility and Environment

## Status

This repository preserves the historical research notebooks without their execution outputs and includes the consolidated five-seed SHAP/LIME explanation-stability evidence in `evidence/`. The published evidence has passed automated internal-consistency verification through GitHub Actions.

The repository is an archival research-code release rather than a fully self-contained, end-to-end executable pipeline. Original datasets, fitted models, and intermediate preprocessing artifacts are not redistributed. A fresh reproduction of the complete experimental workflow has not been independently verified from the published repository alone.

## Verified Experiment Specifications

- **Unit of residential analysis:** 60-minute windows, 30-minute stride, and 23 engineered normalized features.
- **Dataset roles:** NAB provides anomaly-benchmark targets; BLUED provides appliance switching-event targets; UK-DALE and AMPds2 provide unlabeled residential energy measurements.
- **Residential training populations:** UK-DALE contains 218,358 training windows, and AMPds2 contains 441,483 training windows for the frozen Isolation Forest experiments.
- **Frozen residential Isolation Forest:** 300 trees and `max_samples=256`. The source models were functionally reproduced, and their scores were checked against archived experimental records.
- **Explanation target:** `-IsolationForest.decision_function(X)`.
- **Kernel SHAP:** 100 training-only background rows, 300 coalition samples, and 10 nonzero reported contributions. Background sampling seeds were `[42, 123, 456, 789, 2026]`, while coalition-sampling randomness was fixed at seed 42.
- **LIME:** A fixed 8,192-row training reference per dataset, 5,000 perturbations, regression mode, quartile discretization, and 10 selected features. Perturbation seeds were `[42, 123, 456, 789, 2026]`.
- **Five-seed stability experiment:** 13 selected windows × 2 explanation methods × 5 seeds = 130 explanations, yielding 260 pairwise top-five Jaccard comparisons, 2,990 original-feature records, and 26 window-by-method summaries.
- **Statistical aggregation:** The ten pairwise Jaccard values are averaged separately for each window. Dataset-level and overall summaries use the resulting window-level means, with sample standard deviation (`ddof=1`) calculated across windows. Pairwise comparisons are not treated as independent experimental observations.

## Software Records

The final local explanation-reproducibility environment recorded:

- Python: 3.13.18 (archived D5 record)
- NumPy: 2.4.6 (archived D5 record)
- pandas: 2.2.3 (archived D5 record)
- scikit-learn: 1.6.1
- SHAP: 0.54.1
- LIME: 0.2.0.1

These version records originate from the archived evidence and final local verification environment. They should not be interpreted as proof that every historical experiment was executed under the same software configuration.

For the final explanation and auditing subset, refer to `requirements-explanations.txt`.

Historical model-training notebooks may also require TensorFlow, XGBoost, HDF5 support, and other dependencies. Some historical experiments used different package versions and may require environment-specific adjustments.

A single fully pinned environment capable of reproducing every historical experiment has not been independently validated.

## Data and Filesystem

1. Obtain the datasets from their official maintainers and comply with the applicable licenses and usage conditions. BLUED switching-event annotations must not be interpreted as confirmed physical fault labels.
2. Recreate the required preprocessing and historical artifact structure separately. Raw datasets and private experimental artifacts are not included in this repository.
3. Historical notebooks retain environment-specific Google Colab paths, including `/content/drive/MyDrive/Master/Thesis/Code`. Adapt these paths to the local environment before execution.
4. The historical notebook cells were preserved except for a potentially destructive `!rm -rf /content/drive` command, which was replaced with a descriptive Markdown notice in the publication copy.
5. Some notebooks depend on variables, input files, previously generated outputs, and fitted models from earlier experimental sessions. Verify these prerequisites before executing individual cells.
6. Do not execute the entire historical master notebook sequentially without first reviewing its dependencies and filesystem operations.

## Notebook Guide

The historical notebooks are available in:

`notebooks/historical/`

They document the research and experimental development process. Their ordering represents conceptual workflow stages rather than a guaranteed executable dependency chain.

The controlled explanation-stability notebooks are available in:

`notebooks/stability_validation/`

These notebooks were designed to operate within the previously prepared Google Colab research environment. They are not independently executable from a completely fresh runtime without reconstructing the required variables and archived input artifacts.

Checkpoint 5A and 5B source notebooks are not included in this repository. Their experimental provenance is documented in the preserved evidence manifest and consolidated results.

The corrected Checkpoint 6A consolidation notebook is included.

## Published Explanation-Stability Evidence

The `evidence/` directory contains:

- `all_130_explanation_runs.csv` — Run-level SHAP and LIME explanation records.
- `all_2990_original_feature_records.csv` — Original-feature attribution and LIME mapping records.
- `all_260_pairwise_jaccard.csv` — Pairwise top-five feature-set comparisons.
- `window_level_26_method_records.csv` — Stability and fidelity summaries for each window and explanation method.
- `dataset_and_overall_summaries.csv` — Aggregated dataset-level and overall results.
- `evidence_manifest.json` — Experimental provenance and integrity metadata.

The experiment comprises five runs of each explanation method on each of 13 purposively selected residential windows.

### Verified Stability Results

| Dataset | Kernel SHAP Mean ± SD | LIME Mean ± SD |
|---|---:|---:|
| UK-DALE (5 windows) | 1.0000 ± 0.0000 | 0.7924 ± 0.1435 |
| AMPds2 (8 windows) | 0.9667 ± 0.0617 | 0.8500 ± 0.0309 |
| Overall (13 windows) | 0.9795 ± 0.0501 | 0.8278 ± 0.0910 |

The overall mean LIME local-surrogate coefficient of determination was approximately `R² = 0.3484`, indicating limited local surrogate fidelity.

These values describe within-method top-five feature-set stability for the selected windows. They do not establish explanation correctness, physical fault causality, or population-wide generalizability.

## Evidence Validation

The consolidated explanation-stability CSV files are included in `evidence/`.

To validate their numerical consistency, clone this repository and run:

```bash
python scripts/audit_stability.py --evidence-dir evidence
```

The audit script checks the archived explanation counts, feature mappings, SHAP additivity, pairwise Jaccard similarities, and aggregated stability results.

The repository also contains a GitHub Actions workflow named **Verify Thesis Evidence**, which executes the evidence audit and publication-notebook checks.

These checks verify internal numerical consistency. They do not retrain the detectors, independently reproduce the complete historical experiments, or determine whether detected anomalies correspond to real physical faults.

## Reproducibility Limitations

The following limitations must be preserved when interpreting or reusing this repository:

1. The residential datasets do not provide confirmed physical anomaly labels for the evaluated windows.
2. The 13 explanation windows were purposively selected and are not a random sample of all residential windows.
3. SHAP stability was evaluated by varying the training-background sample while fixing coalition-sampling randomness.
4. LIME stability was evaluated by varying perturbation randomness while preserving the training reference and explainer configuration.
5. The original historical Kernel SHAP full attribution vector was not reproduced exactly. The later controlled reconstruction and its five-seed explanations were verified separately.
6. Stable feature-set membership does not guarantee accurate attribution, faithful local surrogate approximation, or causal explanation.
7. Original fitted models and complete historical intermediate artifacts are not distributed with this archival code release.
8. The repository is not claimed to be a fully self-contained, independently reproduced end-to-end benchmark.

For additional publication and provenance details, consult:

- `docs/PUBLICATION_AUDIT.md`
- `docs/RELEASE_CHECKLIST.md`
- `evidence/evidence_manifest.json`
