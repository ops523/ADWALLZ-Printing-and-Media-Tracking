import sqlite3
import os
from datetime import datetime

DB_FOLDER = "database"
DB_NAME = "media_rolls.db"

os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


###############################################################
# CONNECTION
###############################################################

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


###############################################################
# DATABASE INITIALIZATION
###############################################################

def init_database():

    conn = get_connection()
    cur = conn.cursor()

    ###########################################################
    # USERS
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        role TEXT,

        active INTEGER DEFAULT 1

    )
    """)

    ###########################################################
    # SUPPLIERS
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS suppliers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        supplier_name TEXT,

        contact_person TEXT,

        phone TEXT,

        email TEXT,

        created_date TEXT

    )
    """)

    ###########################################################
    # MEDIA ROLLS
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS media_rolls(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        roll_id TEXT UNIQUE,

        supplier TEXT,

        invoice_number TEXT,

        po_number TEXT,

        media_type TEXT,

        roll_width_ft REAL,

        ordered_length_m REAL,

        actual_length_m REAL,

        actual_sqft REAL,

        remaining_sqft REAL,

        status TEXT,

        qr_file TEXT,

        remarks TEXT,

        created_date TEXT

    )
    """)

    ###########################################################
    # PRODUCTION
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS production(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        roll_id TEXT,

        campaign TEXT,

        artwork TEXT,

        printed_sqft REAL,

        operator TEXT,

        production_date TEXT

    )
    """)

    ###########################################################
    # WASTAGE
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS wastage(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        roll_id TEXT,

        category TEXT,

        sqft REAL,

        remarks TEXT,

        created_date TEXT

    )
    """)

    ###########################################################
    # AUDIT LOG
    ###########################################################

    cur.execute("""
    CREATE TABLE IF NOT EXISTS audit_log(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        module TEXT,

        action TEXT,

        reference_id TEXT,

        username TEXT,

        created_date TEXT

    )
    """)

    ###########################################################
    # DEFAULT USER
    ###########################################################

    cur.execute("SELECT COUNT(*) FROM users")

    count = cur.fetchone()[0]

    if count == 0:

        cur.execute("""

        INSERT INTO users(

            username,

            password,

            role

        )

        VALUES(

            ?, ?, ?

        )

        """,

        (

            "admin",

            "$2b$12$ZtVjU2u3kYxQzZQh6C6B5eN6n0Hj9Q7KQn2v6Qm2bKxM8Q9YQWQ5S",

            "Administrator"

        ))

    conn.commit()

    conn.close()


###############################################################
# GENERATE NEXT ROLL ID
###############################################################

def generate_roll_id():

    conn = get_connection()

    cur = conn.cursor()

    year = datetime.now().year

    prefix = f"MR-{year}"

    cur.execute("""

    SELECT roll_id

    FROM media_rolls

    WHERE roll_id LIKE ?

    ORDER BY id DESC

    LIMIT 1

    """, (f"{prefix}%",))

    row = cur.fetchone()

    conn.close()

    if row is None:

        return f"{prefix}-00001"

    last = row["roll_id"]

    number = int(last.split("-")[-1])

    number += 1

    return f"{prefix}-{number:05d}"


###############################################################
# INSERT MEDIA ROLL
###############################################################

def add_media_roll(data):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO media_rolls(

        roll_id,

        supplier,

        invoice_number,

        po_number,

        media_type,

        roll_width_ft,

        ordered_length_m,

        actual_length_m,

        actual_sqft,

        remaining_sqft,

        status,

        qr_file,

        remarks,

        created_date

    )

    VALUES(

        ?,?,?,?,?,?,?,?,?,?,?,?,?,?

    )

    """,

    (

        data["roll_id"],

        data["supplier"],

        data["invoice"],

        data["po"],

        data["media_type"],

        data["width"],

        data["ordered_length"],

        data["actual_length"],

        data["actual_sqft"],

        data["actual_sqft"],

        "OPEN",

        data["qr"],

        data["remarks"],

        datetime.now().strftime("%Y-%m-%d %H:%M")

    )

    )

    conn.commit()

    conn.close()


###############################################################
# GET ALL ROLLS
###############################################################

def get_all_rolls():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    SELECT *

    FROM media_rolls

    ORDER BY id DESC

    """)

    rows = cur.fetchall()

    conn.close()

    return rows


###############################################################
# GET SINGLE ROLL
###############################################################

def get_roll(roll_id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    SELECT *

    FROM media_rolls

    WHERE roll_id=?

    """,

    (roll_id,))

    row = cur.fetchone()

    conn.close()

    return row


###############################################################
# UPDATE BALANCE
###############################################################

def update_remaining_sqft(

        roll_id,

        remaining_sqft

):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    UPDATE media_rolls

    SET remaining_sqft=?

    WHERE roll_id=?

    """,

    (

        remaining_sqft,

        roll_id

    )

    )

    conn.commit()

    conn.close()


###############################################################
# DASHBOARD COUNTS
###############################################################

def dashboard_summary():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    SELECT

        COUNT(*) total_rolls,

        SUM(actual_sqft) total_sqft,

        SUM(remaining_sqft) remaining

    FROM media_rolls

    """)

    row = cur.fetchone()

    conn.close()

    return row
