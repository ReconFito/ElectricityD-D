import sqlite3
from sqlite3 import Error
import os


DB_BASE_PATH = os.path.join(os.path.dirname(__file__), "models")
# conn = sqlite3.connect(os.path.join(DB_BASE_PATH, "comments.db"))
DB_PATH = os.path.join(DB_BASE_PATH, "comments.db")


def create_table(conn):
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS Comment(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            lastname TEXT NOT NULL,
            comment TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def insert_comment(conn, comment):
    try:
        sql = "INSERT INTO Comment(name, lastname, comment) VALUES(?,?,?)"
        cursor = conn.cursor()
        cursor.execute(sql, comment)
        conn.commit()
    except Error as e:
        print(e)

def get_comments(conn:sqlite3.Connection):
    try:
        sql = "SELECT name, lastname, comment FROM Comment"
        cursor = conn.cursor()
        comments = cursor.execute(sql).fetchall()
        return comments
    except Error as e:
        print(e)

def connect(db_file_path):
    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        return conn
    except Error as e:
        print(e)
    return conn