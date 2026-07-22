from database import Base, engine, SessionLocal
from models import User, Warehouse
from utils.security import hash_password


def initialize_database():
    # Create all tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Create default admin
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

        # Create default warehouse
        if db.query(Warehouse).count() == 0:
            db.add(
                Warehouse(
                    warehouse_code="WH001",
                    warehouse_name="Central Warehouse",
                    city="Mumbai",
                    state="Maharashtra",
                    active=True
                )
            )

        db.commit()

    finally:
        db.close()
