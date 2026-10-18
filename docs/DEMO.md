# Five-minute presentation

Disclose at the start: 'This is a fictional repository with intentionally planted
issues. We are demonstrating the review process, not reporting discoveries in
our actual project.'

## 0:00–0:40 — Explain the setup

Show eventlite.py and the intended rules in README. Explain the main agent assigns
work, verifies evidence, and coordinates fixes. Five reviewers have different focuses.

## 0:40–1:20 — Start the agents

Paste the prompt below in a session with repository access and sub-agent support.
Actual agent execution must be visible or supported by saved real output.

> Act as the main agent. Use exactly five sub-agents in parallel to review this
> fictional EventLite repository. Assign: (1) application logic, (2) authorization,
> (3) input validation, (4) data consistency, (5) error handling and test gaps.
> For the initial review inspect eventlite.py and README.md; exclude docs/ANSWER_KEY.md
> and tests/test_regressions.py so you perform a blind review of the planted issues.
> Sub-agents must return findings and evidence without editing files. Consolidate
> and verify findings yourself, then inspect all tests, fix confirmed issues, and
> run the full suite. Preserve intended behaviour and explain each code change.
> Record each agent's actual findings, including overlaps or no findings. Do not
> invent findings or claim tests ran if they did not. Do not commit, push, or deploy.

## 1:20–2:20 — Show review evidence

Use actual completed agent output if the live review takes too long. Show a finding's
file location, trigger, impact, and verification. Do not promise one finding per agent.

## 2:20–4:10 — Demonstrate authorization before/after

Before fixing, run:

```sh
python -c "from eventlite import EventService; print(EventService().cancel(1, 'mallory'))"
```

It currently cancels Alice's event. After a correct fix, the same command should
raise PermissionError. Show the code diff and run the owner/outsider tests:

```sh
python -m unittest discover -s tests -v
```

Do not claim all tests pass until the actual corrected implementation is tested.

## 4:10–5:00 — Explain results

Report verified findings and actual test results. Explain that different focuses
can expose different issues, but parallel agents can overlap or make mistakes.
Human review and test validation remain necessary. Avoid claiming speed gains
without a measured comparison.

## Preparation

Keep the original baseline commit. Save actual agent output, a before/after code
diff, and real test logs for backup. Rehearse once on a fresh branch. Never present
prepared screenshots or previous output as a live run.
