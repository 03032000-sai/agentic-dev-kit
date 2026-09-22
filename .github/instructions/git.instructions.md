---
applyTo: "**/*"
---

# Git Instructions

- inspect branch, status, staged diff, and unstaged diff before Git mutation;
- substantial mutable work belongs on a dedicated feature/fix branch;
- exactly one role owns repository mutation at a time;
- Git Manager is the sole commit writer;
- stage explicit reviewed paths rather than indiscriminate unknown files;
- never reset --hard, clean -fd, discard local work, rewrite history, force push, push, or merge protected/default branches without explicit approval;
- in multi-repo mode, identify the exact repository before every Git operation;
- wrapper and sub-repositories are independent histories.
