from flask import Flask, render_template, redirect
import requests
from database import Database

app = Flask(__name__)

db = Database()

@app.route("/")
def home():
    page_id = 1
    data = db.fetch_PageData(page_id)
    return render_template("main.html", data=data, page_id=page_id)

@app.route("/page=<page_id>")
def pagination(page_id):
    page_id = int(page_id)
    if page_id >= 1:
        data = db.fetch_PageData(page_id)
        return render_template("main.html", data=data, page_id=page_id)
    else:
        return redirect("/404")

if __name__ == "__main__":
    app.run(debug=True)