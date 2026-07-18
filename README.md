# github-app-updater

Download a GitHub release asset, check it, install it, and restart the app. Supports a few restart strategies depending on how you ship (script, frozen binary, etc.).

Wire it up with your repo owner/name and a place to put downloads. Pair with `qtpy-release-chooser` if you want a UI for picking the release.

## Install

```bash
pip install git+https://github.com/bodencrouch/github-app-updater.git
```

Needs `requests` (and usually `pycryptodome` if you verify signatures).

## License

LGPL-3.0-or-later
