# Owner Windows verification — Score Evidence Review

14 November 2026. Owner-reported observations for the standalone extraction from source revision 6f8fbf54be7bc349f44ad3810fbc9409e260a026. Git initialization, initial commit and extracted GitHub CI were pending when these observations were reported. This supplements docs/EXTRACTION_VERIFICATION.md; it does not replace the original extraction-byte manifest.

## Automated checks

| Check | Owner result |
| --- | --- |
| PowerShell installation | Standalone project created at C:\Users\iyad\projects\score-evidence-review. |
| Dependency consistency | pip check: no broken requirements. |
| Extraction source integrity | All recorded SHA256 values matched. |
| Synthetic setup | 72 accounts, 1,380 rows. |
| Python regression | 214 tests and 132 subtests passed; one existing Starlette/AnyIO deprecation warning. |
| Frontend | 20 checks passed, zero failures or skips. |
| Offline case benchmark | 10/10 expected outcomes. |

## Local Docker and browser observations

Demo Compose project: sereview-20261114-204724.

- Account 1000003 at December 1991 reached awaiting review.
- Owner inspected trajectory, frozen evidence and limitations.
- Owner approved with a meaningful reason; decision form disappeared.
- After API container recreation, approved status, reason and frozen evidence persisted. API package hash matched its pre-recreation value. No exact hash is reproduced because none was supplied in this report.
- Absent account 999999999 reached held / incomplete, displayed the missing-account limitation and offered no decision form.
- Shutdown used Compose down without -v. Named volume and private receipt were preserved.

Port 8000 was initially occupied by slack-customer-score-copilot-api-1. That original container was stopped normally, preserving its volume, and remains stopped. This is an owner-local state record, not authorization to restart or remove it.

The local .env contains only the API token and remains private/ignored. .env.example contains a placeholder. Owner cleared shell token/header variables and overwrote clipboard content with harmless text. No credential value is recorded here.

## Explicitly unconfirmed and remaining

Operations refresh and disconnect/reconnect clearing were requested but not separately confirmed. Do not mark them verified for the extracted application. Previous combined-project observations do not fill this gap.

Browser navigation during an in-flight decision and observation of brief queued/running states are not claimed. Automated stale/duplicate decision coverage is distinct from the owner's browser observations.

These results support a first local Git snapshot with the remaining observations documented. They do not close M5.1: independent GitHub CI and the planned Slack repository separation remain outstanding. No new deployment, Azure session, tracker update or project hours are inferred. Azure remains deallocated; the recorded rollback release stays selected. Preserve all original/private databases, volumes, images, backups and activation receipts.

## Record management

SOURCE_MANIFEST.json remains the immutable extraction inventory and hash baseline. This newly added owner-verification document is a later supplemental record and is staged explicitly alongside that baseline. scripts/verify_source.py checks the original extraction files; Git tracks this supplemental record after initialization. Do not regenerate original extraction hashes merely to add verification notes.

## Closure update — 15 November 2026

M5.1 functional verification is complete. Owner Windows checks, both independent
CI results, fresh Slack smoke and case-review Operations/disconnect/reconnect
observations are reconciled in [the closure record](M5_1_Closure_2026-11-15.md).
Earlier pending statements above describe preparation-time status and are
superseded by that dated record. Original extraction hashes remain unchanged.
