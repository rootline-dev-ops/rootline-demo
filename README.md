# rootline-demo

A tiny Python library (`shelf`: pagination and price helpers) with a pytest suite and a GitHub Actions
CI workflow. It exists to demo [Rootline](https://github.com/rootline-dev-ops/rootline) on a real
failing CI run: when `CI` fails on a pull request, the `Rootline` workflow analyses the failed job and
posts the root cause as a PR comment.

```bash
pip install -e ".[dev]" && pytest -v
```
