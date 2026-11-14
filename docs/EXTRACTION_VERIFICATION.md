# Extraction verification

14 November 2026. Assistant checks on the standalone source archive, Linux/Python 3.12.14. No new Git commit or repository was created.

- Clean virtual-environment install of this project's requirements-dev.txt succeeded; pip check passed.
- Final constraints record the clean installed versions plus the existing Windows colorama pin. Original applicable versions are retained; no upgrade was intended.
- Verified synthetic setup: 72 accounts, 1,380 rows. Created only in assistant scratch.
- Python regression: 214 passed, 132 subtests passed, one existing Starlette/AnyIO deprecation warning, no failures.
- Frontend npm clean install/build and all 20 Node checks passed.
- Isolated deterministic benchmark: 10/10 expected outcomes, two warmups excluded. Revision and dirty-state are null because the source is not yet a Git repository; extraction_source_revision records the original source, not a new commit.
- Real local Uvicorn HTTP checks: initial submission and review pause; process restart with same temporary DB; saved-package/idempotency readback; stale/duplicate decisions rejected; approved evidence available; second process restart preserves approved decision and original package hash.
- All six fingerprinted modules match original source bytes. Original source checkout remains unchanged.
- Clean environment has no OpenAI, Anthropic, Slack Bolt, NLTK, scikit-learn or matplotlib installation. Framework transitive dependencies remain present; no provider calls were made.

Initial clean regression found one failure: benchmark required git rev-parse HEAD before repository initialization. Only its metadata handling was adapted: archives report unavailable revision/dirty-state and explicit extraction provenance; actual Git command failures inside an initialized repository still fail. Full regression and benchmark then passed. No fingerprinted module was edited.

Not executed: Windows, PowerShell installer execution, Docker builds/Compose, visual browser inspection or extracted GitHub CI. These remain owner verification. HTTP checks are not visual browser or Docker verification. No Azure resources, owner state, provider or Slack service was contacted. No hours/tracker updates occurred. Original Phase 2 closure remains complete; M5.1 is not closed by these preparation checks.
