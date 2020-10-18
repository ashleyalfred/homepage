from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db= SQL("sqlite:///website.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        db.execute("INSERT into registrants (name, email) VALUES (:name, :email)", name=name, email=email)
        return render_template("response.html", email=email, name=name)