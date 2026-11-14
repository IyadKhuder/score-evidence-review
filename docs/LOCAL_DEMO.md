# Score Evidence Review — local demonstration

14 November 2026. Run only in the new standalone directory. Keep the original checkout unchanged. Use the Python environment from the root README.

## Local demo: prepare, review, decide, restart, read back

Allow roughly 10–15 minutes after the image build. Run from the existing repository
root in PowerShell. Docker Desktop must be running. Free port 8000 first by stopping
its known local server/container normally, preserving its volume. Do not run two
servers on that port. These commands use a new Compose project/volume for each run;
they preserve existing local and Azure stores. Keep the same PowerShell window
throughout so the token, project name and receipt remain available.

```powershell
$py = '.\.venv\Scripts\python.exe'
# The host script uses only Python's standard library.
$run = Get-Date -Format 'yyyyMMdd-HHmmss'
$demoProject = "sereview-$run"
$receipt = "generated/sereview-$run.json"
$env:COPILOT_API_TOKEN = (& $py -c 'import secrets; print(secrets.token_hex(32))').Trim()
if ($LASTEXITCODE -ne 0) { throw 'Token generation failed' }
docker compose -p $demoProject up --build --detach --wait
if ($LASTEXITCODE -ne 0) { throw 'Demo startup failed' }
& $py -m scripts.smoke_api_phase2 prepare --state $receipt
if ($LASTEXITCODE -ne 0) { throw 'Preparation failed; retain receipt and inspect' }
$state = Get-Content -Raw $receipt | ConvertFrom-Json
$caseId = $state.case.case_id
$packageHash = $state.case.package_hash
$headers = @{ Authorization = "Bearer $env:COPILOT_API_TOKEN" }
$caseUrl = "http://127.0.0.1:8000/cases/$caseId"
```

The receipt contains a durable request key, case ID and saved package, not the
token. Keep it private and untracked. `prepare` creates a new synthetic account
1000003 case as of December 1991 and waits for `awaiting_review`. Do not run
`resume` on this receipt: that smoke phase would make the decision automatically.
This demonstration leaves the decision to the analyst.

Open `http://127.0.0.1:8000/`. Copy the generated token to the password field using
a local clipboard, without printing it in a transcript:

```powershell
Set-Clipboard -Value $env:COPILOT_API_TOKEN
```

Paste, then clear the clipboard with `Set-Clipboard -Value ''`. Connect and refresh
the queue. Select the case matching `$caseId`. Inspect the monthly trajectory,
coverage, captured policies, deterministic result, limitations and package binding.
Expect awaiting review / passed / pending. Explain that passed describes completion
of deterministic analysis and is not an LLM quality score. Enter a meaningful
reason, explicitly select approve or reject, and submit once. Observe completed
and the selected analyst decision, with no review form. Acceptance concerns the
saved demonstration package and authorizes no real-world credit action.

Read the saved decision and hash before container replacement:

```powershell
$before = Invoke-RestMethod -Uri $caseUrl -Headers $headers
if ($before.workflow_status -ne 'completed') { throw 'Complete human review first' }
if ($before.analyst_decision -notin @('approved','rejected')) { throw 'Decision missing' }
if ($before.package_hash -ne $packageHash) { throw 'Package changed' }
docker compose -p $demoProject up --detach --force-recreate --wait
if ($LASTEXITCODE -ne 0) { throw 'Restart failed' }
$after = Invoke-RestMethod -Uri $caseUrl -Headers $headers
if ($after.package_hash -ne $packageHash -or $after.analyst_decision -ne $before.analyst_decision -or $after.workflow_status -ne 'completed') { throw 'Preservation check failed' }
```

Reload the browser, reconnect and inspect the same case. Require the same decision,
frozen evidence and hash, with no decision form. Refresh operations; explain that
saved lifecycle counts survive while process-local timing samples restart. No
provider usage or cost is invented. Disconnect and confirm case detail, queue and
operational content clear; reconnect to recover authorized access.

For the insufficient-evidence path, submit an absent synthetic account through the
same authenticated local API. Each run uses a new idempotency key:

```powershell
$heldHeaders = @{ Authorization = "Bearer $env:COPILOT_API_TOKEN"; 'Idempotency-Key' = "m42-held-$run" }
$heldBody = @{ account_id = 999999999; market = 1; as_of_period = '1991-12-01' } | ConvertTo-Json
$held = Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8000/cases' -Headers $heldHeaders -ContentType 'application/json' -Body $heldBody
```

Refresh the queue after processing and select `$held.case_id`. Expect held /
incomplete, inspect the missing-account limitation and require no decision form.
This is an expected boundary, not a successful account assessment. The automated
regression suite separately covers stale/duplicate decisions and held decision
rejection. Browser navigation during an in-flight decision and observation of
brief queued/running states are not claimed by this demonstration.

End the demo, retaining the named volume and image:

```powershell
docker compose -p $demoProject down
if ($LASTEXITCODE -ne 0) { throw 'Local shutdown failed' }
Remove-Item Env:COPILOT_API_TOKEN
Set-Clipboard -Value ''
$headers.Clear()
$heldHeaders.Clear()
```

Never add `-v`, prune images, remove receipts or replace databases. The project name
is `$demoProject`; retaining it allows a later local restart with the same token
configuration and `docker compose -p <recorded-name> up --detach --wait`. A fresh
run uses a new timestamp, volume and receipt. Reusing a timestamp/receipt is not a
fresh demo. If any step fails, stop at that step, retain evidence and shut down the
known local project normally. No Azure commands are part of this walkthrough.

