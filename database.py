from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from config import DATABASE_URL

engine = create_engine(

    DATABASE_URL,

    future=True,

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
