# Publication-preparation audit

## Source preparation completed

- Output content, execution counters, and Colab execution metadata removed from the publication notebooks.
- Historical notebook source retained except one dangerous deletion command in the 625-cell master notebook; this was replaced with an explicit disabled-cell notice.
- No fitted model files, private datasets, or large saved experiment outputs are bundled.
- Initial regex-based scan of code cells found no obvious API tokens, passwords, private keys, or email addresses. **This is not a guarantee that every possible secret has been detected**.
- Notebook filenames normalized; SHA-256 hashes and the disabled-cell provenance are listed in `notebook_source_manifest.json`.

## Risks and non-goals

- The code references historic Colab `MyDrive` paths. This is not itself a credential, but it reduces portability. Readers need to set up their own folders and data.
- The master notebook contains many repeated development cells and should be treated as archival source, not a canonical one-pass pipeline.
- Notebooks may clone public dataset repositories or install dependencies; users should inspect cells before running.
- Dependency conflicts may occur because historical training and final 2026 attribution audits used different environments.
- Raw notebook outputs were cleared, and **the notebooks included in the archive have not been rerun fresh**.
- Checkpoints 5A and 5B source notebooks are not included in this repository. Their experimental provenance is documented in `evidence/evidence_manifest.json`, and the consolidated five-seed SHAP/LIME results are included in the published evidence CSV files.
- The `evidence/` directory contains the consolidated 130 explanation-run records, 2,990 original-feature records, 260 pairwise Jaccard comparisons, and supporting summaries. Their internal numerical consistency has been verified using `scripts/audit_stability.py` and GitHub Actions. These checks do not independently reproduce the full historical training pipeline or validate physical anomaly correctness.
- No new claims of physical fault detection, causal attribution, or population generalization are supported.

## Required independent approvals

- The thesis supervisor has approved making the repository public and citing it in the thesis. This records supervisor permission; it is not an independent determination of institutional intellectual-property ownership.
- Initial public-release licensing decision: no open-source license. Reuse and redistribution rights are not affirmatively granted; third-party licenses remain applicable.
- Check source dataset terms before redistributing any derived time series or large source data; no datasets are included by default.
- Review every staged notebook for accidental personal details or other sensitive strings not caught by automated scanning.
- Validate repository ownership and public-visibility settings.
- Only insert the repository's real public URL into the thesis once the uploaded files have been verified on GitHub.
