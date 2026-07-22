import sqlite3
import os

DB_PATH = "database/media_rolls.db"

os.makedirs("database", exist_ok=True)


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS media_rolls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_id TEXT UNIQUE,
        supplier TEXT,
        width REAL,
        ordered_length REAL,
        actual_length REAL,
        actual_sqft REAL,
        remaining_sqft REAL,
        status TEXT,
        created_date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS production(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_id TEXT,
        campaign TEXT,
        artwork TEXT,
        printed_sqft REAL,
        production_date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS wastage(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_id TEXT,
        reason TEXT,
        sqft REAL,
        created_date TEXT
    )
    """)

    cur.execute("""
    SELECT COUNT(*) FROM users
    """)

    if cur.fetchone()[0] == 0:

        cur.execute("""
        INSERT INTO users(username,password,role)
        VALUES(?,?,?)
        """, ("admin",
              "$2b$12$ZtVjU2u3kYxQzZQh6C6B5eN6n0Hj9Q7KQn2v6Qm2bKxM8Q9YQWQ5S",
              "Administrator"))

    conn.commit()
    conn.close()
