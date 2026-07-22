from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

# Ensure database directory exists
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_URL = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CHANGE_ME"
)

QR_FOLDER = BASE_DIR / "qr_codes"

REPORT_FOLDER = BASE_DIR / "reports"

LOG_FOLDER = BASE_DIR / "logs"

ASSET_PREFIX = {

    "ROLL":"MR",

    "PACKAGE":"PK",

    "TILE":"TL",

    "PRINT_JOB":"PJ",

    "WAREHOUSE":"WH"

}
