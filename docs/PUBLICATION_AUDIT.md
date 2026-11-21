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
- Checkpoints 5A and 5B source notebooks are not included here; their evidence is represented by the original experiment manifest and the consolidated outputs that have not yet been exported into this draft.
- The evidence manifest provides hashes and methodological status, but **without corresponding exported CSVs, third parties cannot independently recompute all findings from this ZIP alone**.
- No new claims of physical fault detection, causal attribution, or population generalization are supported.

## Required independent approvals

- Choose and approve a code license before publishing (none has been invented or implied here).
- Check source dataset terms before redistributing any derived time series or large source data; no datasets are included by default.
- Review every staged notebook for accidental personal details or other sensitive strings not caught by automated scanning.
- Validate repository ownership and public-visibility settings.
- Only insert the repository's real public URL into the thesis once the uploaded files have been verified on GitHub.
