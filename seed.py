from database import SessionLocal
from models import User
from utils.security import hash_password

def seed_database():
    db = SessionLocal()

    if db.query(User).count() == 0:
        db.add(
            User(
                username="admin",
                password=hash_password("admin123"),
                full_name="System Administrator",
                role="Administrator",
                active=True,
            )
        )

    db.commit()
    db.close()
