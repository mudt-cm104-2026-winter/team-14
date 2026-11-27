# Glossary

Short definitions of the words we use in this project.

## Calculator terms

- **Operand** — a number the calculator works on. In `2 + 3`, `2` and `3` are operands.
- **Operator** — the operation between the operands: `+`, `-`, `*`, or `/`.
- **Result** — the number produced by applying the operator, e.g. `5` for `2 + 3`.
- **History entry** — one stored calculation. It keeps the operands, the operator, the result, and an id used by the delete button.
- **History** — the list of entries shown under the form. It is kept in memory, so restarting the server empties it.
- **Filter** — showing only entries with a chosen operator. This changes the view, not the stored history.
- **Newest first** — reverses the history display so the last calculation appears at the top.
- **Validation** — checking input before using it, e.g. making sure both fields contain numbers.
- **Division by zero** — dividing by `0`, which is not allowed. The app shows an error message instead of crashing.

## Git and GitHub terms

- **Issue** — a task tracked on GitHub. Our smaller tasks are sub-issues of three epics.
- **Epic** — a larger issue that groups related sub-issues.
- **Branch** — a separate line of work. We name branches `<issue-id>-short-name`, e.g. `10-docs-glossary`.
- **Commit** — one saved, named step in a branch, e.g. `docs: add glossary`.
- **Clone** — downloading a copy of the repository to your computer.
- **Push** — sending your local commits to GitHub.
- **Pull** — bringing commits from GitHub into your local repository.
- **Pull request (PR)** — a request to merge your branch into `main`, with a description and `closes #n`.
- **Review** — another team member reading the PR diff and commenting on specific lines before approving.
- **Merge** — combining a PR branch into `main`.
- **Merge conflict** — when two branches change the same lines, Git cannot choose automatically. You edit the file, remove the marker lines, commit, and push.
- **Rebase** — moving your commits onto a newer base, so the branch starts from current `main`. Keeps the history tidy.
- **Fast-forward** — a pull where your branch has no local commits of its own, so Git just moves it forward to `main`.
- **Tag** — a named marker for a release. We tag the final `main` as `stage-1`.
- **Virtual environment** — the `.venv` folder holding this project's Python packages, so they do not mix with other projects.
