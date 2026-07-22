"""
Universal Asset Number Generator
"""

from datetime import datetime

from sqlalchemy import func

from database import SessionLocal


def generate_asset_id(model, prefix):

    db = SessionLocal()

    year = datetime.now().year

    count = db.query(func.count(model.id)).scalar()

    count += 1

    asset = f"{prefix}-{year}-{count:06d}"

    db.close()

    return asset
