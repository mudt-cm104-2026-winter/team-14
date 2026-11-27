# How we review

## Branches

- Work on one issue at a time. Start each branch from an up-to-date `main` and name it `<issue-id>-short-name`.
  For example: `12-add-glossary` or `5-delete-single-entry`.
- Do not commit straight to `main`. The branch ruleset requires a pull request and one approval.
- Keep commits small, and write the message as an instruction: `feat: add clear history button`, `fix: handle invalid input`, `docs: add glossary`.
- Push your own branch. Avoid `git push --all`, which can send branches you did not mean to share.

## Pull requests

- One issue, one branch, one PR.
- In the description, say what changed and why, then add `closes #<issue number>` so the issue closes when the PR merges.
- Add one line at the top of `## Unreleased` in `CHANGELOG.md`, with the issue number in brackets, for example `- Add a delete button (#8)`.
- Keep the PR small enough that someone can actually read the diff.
- The author merges after the approval, not before.

## Reviews

- Everyone reviews at least one teammate's PR and leaves at least one inline comment on a specific line in **Files changed**. A plain "looks good" is not enough.
- If something needs fixing, choose **Request changes** and say what should change, pointing at the line where you can.
- The author pushes a fix commit to the same branch, replies to the comment, and asks for another review. The reviewer then approves.
- Comment on the code, not on the person.

## Merge conflicts

If two branches change the same lines of `CHANGELOG.md` or `README.md`:

1. Let the first PR merge.
2. In your branch, run `git fetch origin`, then `git merge origin/main`.
3. Open the file with the conflict markers, keep the lines you need from both sides, and remove the `<<<<<<<`, `=======`, and `>>>>>>>` lines.
4. Commit the result and push your branch again. The PR updates automatically.

## Before we finish

- Each person should have at least two of their own PRs merged.
- Once every PR is merged and all board cards are in Done, tag `main` with `stage-1` and push the tag.
