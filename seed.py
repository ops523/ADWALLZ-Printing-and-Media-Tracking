from database import (
    SessionLocal,
    create_tables
)

from models import (
    Warehouse,
    User
)

from utils.security import hash_password

create_tables()

db = SessionLocal()

#######################################################
# Warehouse
#######################################################

if db.query(Warehouse).count() == 0:

    db.add(

        Warehouse(

            warehouse_code="WH001",

            warehouse_name="Central Warehouse",

            city="Mumbai",

            state="Maharashtra"

        )

    )

#######################################################
# Admin User
#######################################################

if db.query(User).count() == 0:

    db.add(

        User(

            username="admin",

            password=hash_password("admin123"),

            full_name="System Administrator",

            role="Administrator",

            active=True

        )

    )

db.commit()

db.close()

print("Database Initialized")
