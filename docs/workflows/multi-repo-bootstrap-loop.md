# Multi-Repo Bootstrap Loop

Resolve repo URLs → preflight checks → clone into `repos/<name>/` → verify → write manifest → cross-repo dependency discovery → elect anchor repo → hand off to requested workflow.
