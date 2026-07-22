from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

APP_NAME = "AIMS"

VERSION = "1.0.0"

COMPANY = "ADWALLZ"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{BASE_DIR/'database'/'aims.db'}"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CHANGE_THIS_SECRET_KEY"
)
