import sqlite3


def init_db(db_name):
    con = sqlite3.connect(db_name)
    con.row_factory = sqlite3.Row

    try:
        con.executescript('''
    CREATE TABLE user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        password BLOB NOT NULL,
        creation_dt TEXT);

    CREATE TABLE manager(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource TEXT NOT NULL,
        password TEXT NOT NULL,
        comments TEXT,
        user_id INTEGER NOT NULL,
        last_updated TEXT)
    ''')
    finally:
        con.close()