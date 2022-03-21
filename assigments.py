import sqlite3
from flask import jsonify, request

con = sqlite3.connect('backend.db')
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS a (id INT IDENTITY PRIMARY KEY, name TEXT, due_date DATETIME, warn_date DATETIME)"
)


def init(in_app):
    app = in_app

    @app.route("/v1/assignments", methods=["GET"])
    def get_assigments():
        data: map = request.get_json()
        cur.execute(f"SELECT * FROM a ORDER BY warn_date")
        dump = cur.fetchall()
        output = {}
        convert = {1: "assignmentName", 2: "DueDate", 3: "WarnDate"}
        for s in dump:
            for i in range(1, 3):
                output[convert[i]] = dump[i]
        return (jsonify(output))

    @app.route("/v1/assignments", methods=["PUT"])
    def add_assigment():
        data: map = request.get_json()
        cur.execute(
            f"INSERT INTO a (?, ?, ?)",
            [data["assignmentName"], data["DueDate"], data["WarnDate"]])
