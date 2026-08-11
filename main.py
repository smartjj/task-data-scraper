import logging
import os
import sys
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "data-scraper.log"),
    ],
)
log = logging.getLogger("data-scraper")


def run() -> None:
    if not os.environ.get("API_KEY"):
        log.warning("API_KEY is not set")
    if not os.environ.get("DATABASE_URL"):
        log.warning("DATABASE_URL is not set")

    # Placeholder: no scraping target has been defined yet.
    # Replace this block with the real fetch/parse/store logic.
    log.info("no scraping target configured, nothing to do")


def main() -> int:
    log.info("data-scraper task starting")
    try:
        run()
    except Exception:
        log.exception("data-scraper task failed")
        return 1
    log.info("data-scraper task finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
