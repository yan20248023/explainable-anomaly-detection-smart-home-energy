# Explainable Anomaly Detection in Smart Home Energy Systems

Research-code companion for the MSc thesis **Explainable Anomaly Detection in Smart Home Energy Systems**, by **Yanal Idrees**, Princess Sumaya University for Technology.

## Research scope

This offline study investigates **appliance-/electricity-channel-level unusual energy-consumption windows** and **post-hoc explanations of frozen Isolation Forest anomaly scores** using Kernel SHAP and LIME. The study uses different public datasets for different evidence types:

| Dataset | Use in thesis | Meaning of reference labels |
|---|---|---|
| NAB | Supervised and label-blind benchmark experiments | Anomaly-related benchmark targets |
| BLUED | Switching-event benchmark | Appliance switching events, **not confirmed faults** |
| UK-DALE | Unlabeled residential candidate scoring | No confirmed anomaly labels for the evaluated windows |
| AMPds2 | Unlabeled residential channel scoring | No confirmed anomaly labels for the evaluated windows |

The repository does **not** contain a dashboard, user-feedback study, online learning, or live deployment. Physical faults are **not** inferred from model-generated flags or feature attributions.

## Implemented components

- Data standardization, windowing, engineered features, chronological partitioning and split-boundary leakage checks.
- Benchmark models, including supervised classifiers, Isolation Forest, Local Outlier Factor, One-Class SVM, dense/LSTM autoencoders, and a deterministic maximum-absolute-z-score baseline.
- Frozen residential Isolation Forest anomaly scoring and controlled cross-model analysis.
- Model-agnostic Kernel SHAP and regression-mode LIME local explanations on 13 purposively selected residential test windows.
- Five-seed explanation-sampling stability study, without detector retraining or synthetic anomaly injection.

## Verified explanation-stability results

For each of 13 selected windows, five explainer seeds yielded ten within-method top-five-feature-set Jaccard comparisons. The unit of dataset-level aggregation is the **window-level mean**; SD is the sample standard deviation across window means.

| Dataset | Kernel SHAP mean ± SD | LIME mean ± SD |
|---|---:|---:|
| UK-DALE (5 windows) | 1.0000 ± 0.0000 | 0.7924 ± 0.1435 |
| AMPds2 (8 windows) | 0.9667 ± 0.0617 | 0.8500 ± 0.0309 |
| Overall (13 windows) | **0.9795 ± 0.0501** | **0.8278 ± 0.0910** |

The overall mean LIME local-surrogate R² was **0.3484**, indicating limited local surrogate fidelity. Stable feature membership does not establish explanation correctness or physical causality. The original historical Kernel SHAP full attribution vector was **not** reproduced exactly; this limitation remains explicit.

## Contents

- `notebooks/historical/`: output-free copies of the project's historical Colab experiment and audit notebooks.
- `notebooks/stability_validation/`: available controlled validation checkpoints, including the **corrected** 6A consolidation notebook.
- `evidence/evidence_manifest.json`: preserved integrity/provenance summary for the completed stability analysis.
- `scripts/audit_stability.py`: recomputes explanation-set overlap and counts from exported consolidated evidence files.
- `docs/REPRODUCIBILITY.md`: dataset, environment, dependency, notebook, and evidence instructions.
- `docs/PUBLICATION_AUDIT.md`: what was removed, what was not verified, and what still needs to be checked.
- `docs/RELEASE_CHECKLIST.md`: approval steps before publishing.

## Important reproducibility qualifications

**This is an archival, code-centered research repository, not a standalone one-click benchmark.** The historical notebooks reference an existing Google Colab/Drive layout and external datasets, intermediate processed files, and previously fitted artifact files that are not redistributed here. Several notebooks reflect an iterative development history and should not be executed blindly in their displayed order. See `docs/REPRODUCIBILITY.md` before attempting a rerun.

The repository includes the verified consolidated explanation-stability evidence for all 13 selected residential windows: 130 explanation runs, 2,990 original-feature records, 260 pairwise top-five Jaccard comparisons, 26 window-by-method summaries, and six dataset-level and overall summaries. These records are available in the `evidence/` directory, together with the provenance manifest.

The consolidated evidence is automatically checked using GitHub Actions and `scripts/audit_stability.py`. These checks validate the archived explanation results and their internal numerical consistency; they do not retrain the anomaly detectors or establish the physical correctness of detected anomalies.

> Licensing is not yet declared: a license should be chosen and approved before public publication. Dataset copyright and source licenses remain with their respective owners.
