# Score Evidence Review

A durable analyst-review workflow for synthetic score trajectories.

Submit a structured account/month request, inspect deterministic analysis and frozen evidence, then approve or reject the exact saved package with a reason. LangGraph orchestrates durable review; FastAPI serves the authenticated API and TypeScript UI; SQLite stores cases and checkpoints. The UI provides queue, evidence, decisions and operations views. Submission uses the API or supplied tools; there is no case-creation form.

All accounts, histories and policies are invented. This is a portfolio and learning demonstration, not a calibrated credit model or production lending system. Approval accepts the demonstration package and authorizes no credit action. Live notes are disabled; there is no autonomous LLM investigation or Slack bridge.

## Start locally on Windows

Extract the supplied source into a new directory, or clone this project's repository once published. From its root in PowerShell, with Python 3.11/3.12:

```powershell
py -3.11 -m venv .venv
$py = '.\.venv\Scripts\python.exe'
& $py -m pip install -r requirements-dev.txt
if ($LASTEXITCODE -ne 0) { throw 'Install failed' }
& $py -m pip check
if ($LASTEXITCODE -ne 0) { throw 'Dependency check failed' }
& $py scripts/verify_source.py
if ($LASTEXITCODE -ne 0) { throw 'Source integrity check failed' }
```

Docker Desktop must be running and port 8000 free. Follow [the current local demonstration](docs/LOCAL_DEMO.md) to build, submit, review and verify preservation using a fresh project/volume. Docker builds the frontend and verifies/builds synthetic source data; no host Node or data-loader run is needed for that route. Keep existing project volumes and databases intact.

## Source development and checks

In a fresh checkout only, build the synthetic source database, then run offline checks:

```powershell
& $py -m src.data_loader
if ($LASTEXITCODE -ne 0) { throw 'Synthetic setup failed' }
& $py -m pytest -q -rs
if ($LASTEXITCODE -ne 0) { throw 'Tests failed' }
& $py -m scripts.benchmark_cases_phase2 --output generated/benchmark-01.json
if ($LASTEXITCODE -ne 0) { throw 'Benchmark failed' }
Push-Location frontend
try {
    npm ci --ignore-scripts
    if ($LASTEXITCODE -ne 0) { throw 'Frontend install failed' }
    npm test
    if ($LASTEXITCODE -ne 0) { throw 'Frontend checks failed' }
} finally { Pop-Location }
```

Use a new benchmark filename each run. Expected default benchmark: 10/10 outcomes, including correct held cases. This measures two defined in-process HTTP/worker paths, not hosted throughput or model quality. On Linux, create a venv and use its Python for the same module commands. Dependency installation needs network access; case analysis needs no provider or Slack credentials.

## Architecture and limits

The service freezes score observations and seven policy texts before analysis. Compiled deterministic rules evaluate captured rows; policy text supplies provenance rather than executable rules. A single worker uses LangGraph checkpoints, pauses for human review, and binds decisions to the displayed revision and package hash. Stale/conflicting decisions are rejected. Interrupted analysis without a saved result is held instead of blindly replayed.

One process/worker, local SQLite and one shared analyst token are demonstration limits. No multi-replica/HA or per-user role separation is claimed. Requests cover market 1, baseline policies v1.0 and one account/month. Missing evidence can correctly produce a hold. Backups are manual. Durable lifecycle history survives restart; bounded request/stage timing samples reset. Provider usage and monetary cost are unavailable.

[Documentation index](docs/README.md) · [Source provenance](SOURCE_PROVENANCE.md) · [Extraction verification](docs/EXTRACTION_VERIFICATION.md)

## Related project and delivery history

The related [Customer Score Copilot](https://github.com/IyadKhuder/customer-score-copilot) provides bounded English requests, Slack integration, retrieval and optional independently checked LLM claims. These applications share synthetic foundations but install independently.

The original application demonstrated owner-observed Azure delivery, rollback and saved-state recovery. Azure remains deallocated, no public IP, guard disarmed, and the recorded rollback release remains selected. Included delivery tools retain historical names; do not run provisioning or deployment to complete this extraction. See [delivery scope](docs/DELIVERY_SCOPE.md).

## License

[MIT](LICENSE), copyright 2026 Iyad Khuder. Third-party dependencies retain their own licenses.
