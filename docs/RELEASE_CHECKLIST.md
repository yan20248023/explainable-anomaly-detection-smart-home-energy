# Release checklist

- [ ] Personally review cleaned notebook source, especially cells that mount Drive, access files, download external resources, or write artifacts.
- [ ] Decide whether the historical development notebooks should be public in full or moved to a separate archival release.
- [ ] Confirm redistribution rights and choose an appropriate code license.
- [ ] Decide whether to publish the **consolidated derived evidence** after checking data licenses; it is not included in this starter ZIP.
- [ ] If publishing evidence, export the five files listed in `docs/REPRODUCIBILITY.md` and run the `scripts/audit_stability.py` verification.
- [ ] Confirm README author, institutional affiliation and research claims.
- [ ] Connect GitHub and create a **public** repository only after reviewing the above.
- [ ] Upload the reviewed repository contents and verify that the files, README and code are accessible anonymously.
- [ ] Record the actual repository URL, optionally tag `v1.0.0` and create a stable release.
- [ ] Add the verified URL to the manuscript's reproducibility/code-availability section and recompile Overleaf.
