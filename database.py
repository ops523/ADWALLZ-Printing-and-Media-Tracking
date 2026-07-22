"""
database.py
----------------------------------------
Database configuration for AIMS

Supports:

1. SQLite (Development)

2. PostgreSQL (Production)

Author:
ADWALLZ ERP
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import QueuePool
from config import DATABASE_URL
import os

# ----------------------------------------------------
# Ensure database folder exists for SQLite
# ----------------------------------------------------

if DATABASE_URL.startswith("sqlite"):

    os.makedirs("database", exist_ok=True)

# ----------------------------------------------------
# SQLAlchemy Engine
# ----------------------------------------------------

engine = create_engine(

    DATABASE_URL,

    poolclass=QueuePool,

    pool_size=10,

    max_overflow=20,

    future=True,

    echo=False

)

# ----------------------------------------------------
# Session Factory
# ----------------------------------------------------

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)

# ----------------------------------------------------
# Base Class
# ----------------------------------------------------

Base = declarative_base()

# ----------------------------------------------------
# Dependency
# ----------------------------------------------------

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# ----------------------------------------------------
# Create Database
# ----------------------------------------------------

def create_database():

    from models import (
        User,
        Supplier,
        MediaType,
        MediaRoll,
        Production,
        Wastage,
        AuditLog
    )

    Base.metadata.create_all(bind=engine)

# ----------------------------------------------------
# Health Check
# ----------------------------------------------------

def test_connection():

    try:

        conn = engine.connect()

        conn.close()

        return True

    except Exception as e:

        print(e)

        return False
