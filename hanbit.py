from flask import Flask
from flask import request
import json
import sqlite3

app = Flask(__name__)
app.debug = True

def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("db.sqlite3")

@app.route("/")
def hello():
    with get_db_con() as con:
        cur = con.cursor()
        q = "select * from hanbit_books"
        result = cur.execute(q)
    result_json = jsonize(result)
    return result_json

@app.route("/books/by/author")
def get_books_by_author():
    name = request.args.get("name")
    with get_db_con() as con:
        cur = con.cursor()
        q = "SELECT * FROM hanbit_books WHERE author LIKE :name ORDER BY title"
        param = {
            "name": "%" + name + "%"
        }
        result = cur.execute(q, param)
    result_json = jsonize(result)
    return result_json

@app.route("/books/by/month")
def get_books_by_month():
    month = request.args.get("month")

    if int(month) < 10:
        month = "0" + month
    
    with get_db_con() as con:
        cur = con.cursor()
        q = "SELECT * FROM hanbit_books WHERE strftime('%m', pub_date) = :month ORDER BY pub_date DESC"
        param = {
            "month": month
        }
        result = cur.execute(q, param)
    result_json = jsonize(result)
    return result_json

def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json

if __name__ == "__main__":
    app.run()