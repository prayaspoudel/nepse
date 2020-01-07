import sqlite3

conn = sqlite3.connect('a.db')
db = conn.cursor()

db.executemany()