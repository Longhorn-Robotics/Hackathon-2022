import sqlite3

con = sqlite3.connect('backend.db')
cur = con.cursor()

cur.execute(
    "CREATE TABLE users (id INT PRIMARY KEY, email TINYTEXT, name TEXT, password TEXT, discord_id INT, canvas_token TEXT)"
)
