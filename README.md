# Stacked PR Platform Demo

This repository demonstrates stacked pull requests with a small Python platform workload. Each branch adds one reviewable capability and targets the branch immediately below it.

## Stack

| Order | Branch | Change | Pull request base |
| --- | --- | --- | --- |
| 1 | `stack/01-health-api` | Flask service with health endpoints and tests | `main` |
| 2 | `stack/02-container` | Container image and local Compose workflow | `stack/01-health-api` |
| 3 | `stack/03-kubernetes` | Kubernetes deployment, service and probes | `stack/02-container` |
| 4 | `stack/04-observability` | Prometheus metrics and ServiceMonitor | `stack/03-kubernetes` |

The final branch contains the complete project. See [`docs/STACKED_PRS.md`](docs/STACKED_PRS.md) there for the GitHub and Bitbucket workflows.

## Explore locally

```bash
git log --graph --decorate --oneline --all
git diff main...stack/01-health-api
git diff stack/01-health-api...stack/02-container
git diff stack/02-container...stack/03-kubernetes
git diff stack/03-kubernetes...stack/04-observability
```

## Purpose

This is an educational repository. The branch history is the main deliverable: clone it, inspect each incremental diff, and practice opening dependent pull requests in order.
