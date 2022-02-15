import sqlite3 as sq
with sq.connect("file_manager.db") as con:
    cur = con.cursor()
    cur.execute('')

