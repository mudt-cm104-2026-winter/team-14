# Calculator with history

## What this is

A small web calculator for our CM-104 team project. You enter two numbers, pick `+`, `-`, `*` or `/`, and the app shows the result and keeps a list of past calculations. You can filter the list by operator, reverse the order, delete one row, or clear everything. It is a simple app meant for practising Git and GitHub together, not a production calculator.

## How to run it

You need Python 3.10 or newer. The full walkthrough is in [docs/how-to-run.md](docs/how-to-run.md).

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop the server with `Ctrl+C`.

The entries are kept in memory, so the history is empty again after a restart.

## Team

| GitHub | Role |
|---|---|
| usarikurk | App code, history features and documentation |

## How we work

- One issue, one branch, one pull request. Branches start from an up-to-date `main` and are named `<issue-id>-short-name`, e.g. `12-add-glossary`.
- We do not commit straight to `main`. Every PR needs a description with `closes #n` and one line in `CHANGELOG.md`.
- Another team member reviews each PR and leaves an inline comment on a specific line before approving. If something needs fixing, the reviewer requests changes and the author pushes a fix commit.
- The author merges after approval. When two branches touch the same lines, we pull `main` into the branch, resolve the conflict, then commit and push.
- Longer guides live in `docs/`: [how to run](docs/how-to-run.md), [how we review](docs/how-we-review.md), and the [glossary](docs/glossary.md).

## Sources

- 2026-11-05: `assessment-1-team-project.md` (CM-104 stage-1 brief), used for the required README sections and the final checklist.
- 2026-11-27: the `README.md` template and `requirements.txt` in this repository, used for the setup steps and pinned package versions.

## Use of AI

- 2026-11-27: OpenCode (Big Pickle), used to plan the consecutive issues (order, branch names and PR steps) and to draft the guides in `docs/`. Checked by comparing the plan with the GitHub issues, and by reading the docs against `requirements.txt` and the existing files before committing.
