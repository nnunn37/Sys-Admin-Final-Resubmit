from flask import Flask
from flask import render_template
from flask import url_for
from flask import request, flash

import sqlite3 as sql

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return "Hello and Welcome to the Cansdale High School website. For all the information you need, please use the /index page."



@app.route("/index/")
def index_page():
    return render_template("index.html")

@app.route("/contact/")
def contact_page():
    return render_template("contact.html")

@app.route("/email/")
def email_page():
    return render_template("email.html")

@app.route("/staff/")
def staff_page():
    return render_template("staff.html")

@app.route("/student")
def new_student():
    return render_template("student.html")

@app.route("/addrec", methods=["POST"])
def addrec():
    if request.method == "POST":
        name = request.form["nm"]
        addr = request.form["add"]
        city = request.form["cty"]

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name, address, city) VALUES (?, ?, ?)", [name, addr, city])
        con.commit()

        return render_template("list.html")

@app.route("/boot")
def boot_demo():
    return render_template("boot.html")


if __name__ == '__main__':
    app.run(debug=True)