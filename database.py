from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from config import DATABASE_URL

engine = create_engine(

    DATABASE_URL,

    future=True,

    pool_size=10,

    max_overflow=20,

    pool_pre_ping=True,

    echo=False

)
SessionLocal = sessionmaker(

    bind=engine,

    autoflush=False,

    autocommit=False

)

Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
