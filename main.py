import sqlite3 as sq
with sq.connect("file_manager.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    surname TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS favourite_paths (
    path TEXT,
    added DATE,
    id INTEGER PRIMARY KEY AUTOINCREMENT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS users_to_path (
    user_id INTEGER,
    path_id INTEGER,
    FOREIGN KEY (user_id)  REFERENCES users(id),
    FOREIGN KEY (path_id)  REFERENCES favourite_paths(id))""")
