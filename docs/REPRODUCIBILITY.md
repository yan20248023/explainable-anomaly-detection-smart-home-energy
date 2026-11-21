# Reproducibility and environment

## Status

This repository preserves available historical source notebooks without their outputs. **Code-source inspection is not equivalent to a verified fresh end-to-end rerun.** The reported stability study was verified against frozen research artifacts; those artifacts and the full source datasets are not included in this draft.

## Verified experiment specifications

- Unit of residential analysis: 60-minute windows, 30-minute stride, 23 engineered normalized features.
- Dataset roles: NAB anomaly-benchmark targets, BLUED switching-event targets, UK-DALE and AMPds2 unlabeled residential series.
- UK-DALE: 218,358 training windows; AMPds2: 441,483 training windows for frozen residential Isolation Forest experiments.
- Frozen residential Isolation Forest: 300 trees, max_samples=256; source models were functionally reproduced and scored against archived records.
- Explanation target: `-IsolationForest.decision_function(X)`.
- Kernel SHAP: 100 training-only background rows, 300 coalition samples, 10 reported nonzero contributions; background seeds `[42,123,456,789,2026]`, coalition RNG fixed at 42.
- LIME: fixed 8,192 training-reference rows per dataset, 5,000 perturbations, regression mode, quartile discretization and 10 selected features; perturbation RNG seeds `[42,123,456,789,2026]`.
- Five-seed stability: 13 × 2 × 5 = 130 runs; 260 pairwise top-five-set Jaccard values; 2,990 original-feature rows; 26 window-method summaries.
- Statistical aggregation: compute the mean Jaccard of ten seed pairs **per window**, then sample SD (`ddof=1`) across windows. Do not treat ten pairs as independent research samples.

## Software records

The final local LIME and SHAP reproducibility environment recorded scikit-learn 1.6.1, SHAP 0.54.1 and LIME 0.2.0.1. The archived D5 evidence recorded Python 3.13.18, NumPy 2.4.6, pandas 2.2.3. Some historical notebooks used other dependency versions and are not covered by one fully pinned, revalidated environment.

For the final explanation/audit subset, install the versions in `requirements-explanations.txt` in an appropriate Python environment. Historical model training uses other packages (TensorFlow, XGBoost, HDF5 support, etc.) and may require version-specific adjustments.

## Data and filesystem

1. Obtain datasets from the **official dataset maintainers** according to their respective license/usage terms. Do not interpret BLUED switch events as fault labels.
2. Recreate the input preprocessing and historical artifact structure separately; no private user Drive folder is embedded in the repository.
3. **Historical notebooks contain Colab-style absolute paths** such as `/content/drive/MyDrive/Master/Thesis/Code`. Update these paths for your environment before executing cells.
4. All notebook cells were preserved except a dangerous `!rm -rf /content/drive` command, which was replaced by a descriptive markdown notice in the publication copy.
5. Notebooks may assume variables, files, output folders and fitted models created in prior sessions. Read and validate prerequisites before running cells. Do not run the full master notebook top-to-bottom without reviewing it.

## Notebook guide

The historical notebooks in `notebooks/historical/` are ordered as conceptual workflow stages, not as a guaranteed executable dependency chain. The stability notebooks are self-contained cells only with respect to variables and files from the **previously prepared Colab runtime**. In this draft, checkpoint 5A and 5B source notebooks are not present locally; their source/output verification is represented in the preserved provenance manifest. The corrected consolidation 6A notebook is included.

## Evidence validation

The file `evidence/evidence_manifest.json` includes the hash fingerprint of the completed stability protocol:

`849e9d7ef15cc3b135ac74854f491ae3c2113f39c3ef527ca789cde8e829334c`

The consolidated 6A outputs in the original research Drive have the filenames:

- `all_130_explanation_runs.csv`
- `all_2990_original_feature_records.csv`
- `all_260_pairwise_jaccard.csv`
- `window_level_26_method_records.csv`
- `dataset_and_overall_summaries.csv`

Place copies of those files in a local directory and run:

```bash
python scripts/audit_stability.py --evidence-dir /path/to/exported/consolidated/evidence
```

This recomputes counts, feature identities, per-window pairwise overlaps and grouped mean ± sample SD. A full end-to-end reproduction additionally requires access to original dataset contents, preprocessing artifacts, and fitted detectors.
