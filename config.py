from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

APP_NAME = "AIMS ERP"

COMPANY = "ADWALLZ"

VERSION = "1.0"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{BASE_DIR/'database'/'aims.db'}"
)

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
