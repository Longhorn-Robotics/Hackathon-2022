from flask import jsonify, request
from app import app
import sqlite3

con = sqlite3.connect('backend.db')
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, email TINYTEXT UNIQUE, name TEXT, password TEXT, discord_id INT, canvas_token TEXT)"
)


@app.route("/v1/login", methods=["CREATE"])
def create_user():
    data: map = request.get_json()
    if data["email"] and data["password"]:
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                    data["email"], data["password"])
    return (jsonify(request.get_json()))
