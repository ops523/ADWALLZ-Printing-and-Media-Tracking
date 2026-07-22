"""
Initial Master Data
"""

from database import SessionLocal

from models import Warehouse

db = SessionLocal()

if db.query(Warehouse).count() == 0:

    db.add(

        Warehouse(

            warehouse_code="WH001",

            warehouse_name="Central Warehouse",

            city="Mumbai",

            state="Maharashtra"

        )

    )

    db.commit()

db.close()
