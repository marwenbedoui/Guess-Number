import sqlite3
from datetime import datetime

DATABASE_NAME = 'game_attempts.db'

def create_table():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS attempts (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          attempts INTEGER,
                          date TEXT)''')
        conn.commit()

def store_attempt(attempts):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO attempts (attempts, date) VALUES (?, ?)", (attempts, date))
        conn.commit()

def fetch_attempts():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attempts")
        return cursor.fetchall()
    