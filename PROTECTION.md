# Branch Protection Rules - SmartBin

## Overview
This document explains the branch protection rules implemented for the `main` branch.

## Protection Rules

| Rule | Setting | Reason |
|------|---------|--------|
| Require pull request reviews | 1 reviewer required | Ensures code quality |
| Require status checks to pass | CI workflow must pass | Prevents merging broken code |
| Disable direct pushes | All changes via PR | Forces code review |

## Why These Rules Matter

1. **Quality Assurance** - No code reaches main without review
2. **Team Collaboration** - Encourages code review
3. **CI/CD Integration** - Automated tests run on every PR

## How to Contribute

1. Create a feature branch from main
2. Make changes and push
3. Open a Pull Request
4. Wait for CI tests to pass
5. Request review
6. Merge after approval and passing tests
