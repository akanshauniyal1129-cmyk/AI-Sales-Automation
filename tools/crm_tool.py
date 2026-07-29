import sqlite3
from datetime import datetime
import os
DB_FOLDER="database"
DB_PATH=os.path.join(DB_FOLDER, "leads.db")

def create_database():
    os.makedirs(DB_FOLDER, exist_ok=True)
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS leads(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            industry TEXT,
            email TEXT,
            status TEXT,
            follow_up_date TEXT
            )
        """)
    conn.commit()
    conn.close()

def save_lead(company_name, industry, email):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute(
        """
        INSERT INTO leads
        (
        company_name,
        industry,
        email,
        status,
        follow_up_date
        )
        VALUES (?,?,?,?,?)
        """,
        (
            company_name, industry, email, "New Lead", datetime.now().strftime("%Y-%m-%d"))

    )
    conn.commit()
    conn.close()
    return "Lead Saved Successfully"