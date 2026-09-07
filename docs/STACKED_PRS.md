# Reproducing the stacked pull request workflow

## Why this repository uses a stack

The final change introduces an application, container packaging, Kubernetes deployment, and monitoring. One pull request would mix four review concerns. The stack lets application, container, platform, and observability changes be reviewed independently.

## Push all branches

```bash
git push -u origin main
git push -u origin stack/01-health-api
git push -u origin stack/02-container
git push -u origin stack/03-kubernetes
git push -u origin stack/04-observability
```

## GitHub CLI

`gh` manages GitHub pull requests; it is not a replacement for `git`.

```bash
gh pr create --head stack/01-health-api --base main \
  --title "[1/4] Add health API" --body "First PR in the stack."

gh pr create --head stack/02-container --base stack/01-health-api \
  --title "[2/4] Containerize the API" --body "Depends on PR 1."

gh pr create --head stack/03-kubernetes --base stack/02-container \
  --title "[3/4] Deploy to Kubernetes" --body "Depends on PR 2."

gh pr create --head stack/04-observability --base stack/03-kubernetes \
  --title "[4/4] Add Prometheus monitoring" --body "Depends on PR 3."
```

## Bitbucket

Push the same branches with `git`. In Bitbucket, create each pull request with the source and destination branches shown in the table in the root README. The stack itself is hosting-platform independent; only PR creation differs.

## After a lower PR merges

Retarget the next PR to `main`. If the repository uses squash merges, rebase the remaining branch because the squash commit has different ancestry:

```bash
git switch stack/02-container
git rebase --onto main stack/01-health-api stack/02-container
git push --force-with-lease
```

Repeat the operation upward through the stack. Coordinate before rewriting a shared branch, and check repository permissions because some organisations prohibit force pushes.

## Review each incremental diff

```bash
git diff main...stack/01-health-api
git diff stack/01-health-api...stack/02-container
git diff stack/02-container...stack/03-kubernetes
git diff stack/03-kubernetes...stack/04-observability
```
