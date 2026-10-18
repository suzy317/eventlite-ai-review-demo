# EventLite: five-agent code review demo

A fictional Python event-booking service, separate from ConnectSphere.
This code deliberately contains bugs for a classroom demonstration. All identities
are fictional. It is a local service object, not a website or production system.
It has no network listener, login system, external services, or real credentials.
The `actor` parameter represents a caller identity supplied by a trusted layer.

## Run (Python 3.10+, no packages required)

```sh
python eventlite.py
python -m unittest discover -s tests -p test_smoke.py -v
python -m unittest discover -s tests -p test_regressions.py -v
```

On some computers use `python3`. Run commands from this folder.
Baseline: 3 smoke tests pass. The 5 regression test methods fail or error on
purpose; they describe the intended behaviour. One has multiple failing subtests.
After the review and fixes, run the complete suite:

```sh
python -m unittest discover -s tests -v
```

## Intended rules

- An event cannot exceed capacity.
- Only the event owner can cancel it; unauthorized attempts raise PermissionError.
- Capacity must be a positive integer; booleans are not valid capacities.
- A failed transfer must leave the original registration intact.
- Unknown event IDs raise ValueError('Event not found').

## Put it on GitHub

Create an empty repository named `eventlite-ai-review-demo`, extract this ZIP,
and upload the contents of this folder (including tests and docs). Alternatively,
from this folder, after creating the empty remote:

```sh
git init
git add .
git commit -m "Add intentionally flawed EventLite demo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/eventlite-ai-review-demo.git
git push -u origin main
git switch -c demo/ai-code-review
```

Replace YOUR_USERNAME. No GitHub repository was created by generating this ZIP.
See docs/DEMO.md for the prompt and presentation sequence. The answer key is
separate from the main source; ask reviewers to exclude it for a blind review.
