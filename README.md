# github-app-updater

Core library for GitHub release auto-updates: asset download, crypto verify, install, restart.

## Install

```bash
pip install -e .
# or from GitHub:
pip install git+https://github.com/bodencrouch/github-app-updater
```

## Origin

Extracted from the [PyKotor](https://github.com/bodencrouch/PyKotor) monorepo `utility` / related packages.
KotOR-specific couplings were removed or made optional for standalone use.

### DAG
Optional: `loggerplus`, `app-process-lifecycle`. Qt UI lives in `qtpy-release-chooser`.

## License

LGPL-3.0-or-later
