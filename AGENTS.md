# Workspace notes

`D:\Ai Tasks` is a git repo with no commits yet; root `git status` shows only untracked top-level folders. Several folders are independent nested git repos. Check `git status` inside the folder you change — root-level git output will not show those file-level changes.

## Project map

- `Meeting Room Booking System/` — own git repo (`main`, `origin/main`) and its own `AGENTS.md`; follow it. Stdlib-only; `python -m unittest discover -v` from that folder (14 tests).
- `Day 8 Abbireddy Naga Bhargavi/` — flat FastAPI exercise, no nested git repo. Use `.\.venv\Scripts\python.exe -m pytest -q` from that folder (1 test). `main.py` imports top-level `utils`/`config`, so run the app from that folder, not from the workspace root. `task_manager.py` is a standalone example, not wired into the API.
- `Day 8 Abbireddy Naga Bhargavi/fs-api/` — separate uv project (`uv.lock`, `.python-version` = 3.14, `src/fs_api`). Run the console script with `uv run fs-api` (`fs-api = fs_api:main`); no tests, so don't run the parent pytest suite here.
- `Day 7 Challenge/support-bot/` — Flask + fake-LLM security exercise with `.venv`; `.\.venv\Scripts\python.exe -m pytest -q` gives 5 tests (README's "3 tests" is stale). `tests/conftest.py` puts the app dir on `sys.path` and creates `logs/`; `app.py` logs to relative `logs/app.log`, so keep cwd at the app root. CI (`.github/workflows/ci.yml`) uses Python 3.12 + pip; local venv is 3.14.
- `day 7 Abbireddy Naga Bhargavi/Day-7-git-practice-Task/Day7-Support-Bot/` — same `app.py`/tests as the challenge app but with no `.venv`; `pip install -r requirements.txt` then `python -m pytest -q` from that folder. Parent repo is on branch `day7-support-bot` with an origin.
- `day 7 Abbireddy Naga Bhargavi/Day-7-git-practice-Task/Hands-on-7-Secrets/` — separate nested repo; `.env` with `API_KEY` is gitignored and loaded by `python-dotenv`. Never print or commit its value.
- `Day 9 FS01/` — empty.

## Verification rules

- No root-level build, test, lint, formatter, typecheck, codegen, or CI config; verify in the touched project directory.
- Local interpreter is Python 3.14.10; docs/specs that say 3.12 describe a target, not an installed runtime. `fs-api` pins 3.14; support-bot CI pins 3.12.
