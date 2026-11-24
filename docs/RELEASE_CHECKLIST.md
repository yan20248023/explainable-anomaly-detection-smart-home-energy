
# Research Code — Final Release Checklist

## Completed Preparation

- [x] Create the private GitHub repository.
- [x] Upload the cleaned historical research notebooks.
- [x] Remove saved notebook outputs and execution counters.
- [x] Disable the potentially destructive notebook deletion command.
- [x] Upload the consolidated five-seed SHAP/LIME evidence.
- [x] Verify the 130 explanation runs, 2,990 feature records, and 260 pairwise Jaccard comparisons.
- [x] Pass the GitHub Actions automated verification workflow.
- [x] Update README.md with the evidence description.
- [x] Update reproducibility and publication-audit documentation.
- [x] Document the limitations of independent reproduction.

## Before Public Release

- [ ] Complete a final manual review of notebook source code and repository contents for sensitive information.
- [ ] Confirm that publishing the included research code and derived evidence is permitted.
- [ ] Document the software licensing decision. Do not assume that an MIT License is authorized.
- [ ] Confirm that no private datasets, fitted model artifacts, or credentials are included.
- [ ] Confirm that all repository documentation accurately describes the released contents.

## Public Repository Verification

- [ ] Change repository visibility from Private to Public after the release checks.
- [ ] Verify that the repository and evidence files are accessible without signing in.
- [ ] Confirm that the public GitHub Actions verification passes.
- [ ] Record the final public repository URL.

## Thesis Integration

- [ ] Add Appendix D: Research Code and Reproducibility Resources.
- [ ] Include the verified public GitHub repository URL.
- [ ] Describe the archived notebooks, evidence files, verification scripts, and reproducibility limitations.
- [ ] Recompile the thesis in Overleaf.
- [ ] Confirm that Appendix D appears correctly in the table of contents.
- [ ] Submit the updated thesis for Prof. Rawan's final approval.
