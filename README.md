# task-data-scraper

Example task submodule for [main-task-manager](https://github.com/smartjj/main-task-manager).
Runs on a schedule via GitHub Actions (`.github/workflows/task.yml`, every 6 hours).

## Status

Placeholder — `main.py` runs, logs, and exits successfully, but has no real
scraping logic yet. No target source, fields, or storage destination have
been defined.

## Extending

1. Add dependencies to `requirements.txt`.
2. Implement the fetch/parse/store logic in `run()` inside `main.py`.
3. Configured secrets available as env vars: `API_KEY`, `DATABASE_URL`.
   Non-secret: `LOG_LEVEL`.

## Local run

```bash
pip install -r requirements.txt
python main.py
```

Logs are written to stdout and `logs/data-scraper.log`; on workflow failure
the `logs/` directory is uploaded as a build artifact.
