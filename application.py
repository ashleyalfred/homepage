from flask import Flask, render_template, request
import sqlite3

# import smtplib
# from email.message import EmailMessage


app = Flask(__name__)

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
        subject = request.form.get("subject")
        message = request.form.get("message")
        conn = sqlite3.connect('website.db')
        c = conn.cursor() 
        c.execute("INSERT into registrants (name, email, subject, message) VALUES (?, ?, ?, ?)", (name, email, subject, message))
        conn.commit()
        conn.close()
        # msg = EmailMessage()
        # msg.set_content(message)
        # msg['Subject'] = subject
        # msg['From'] = "ashley@sagerecruiting.me"
        # msg['To'] = "ashley@sagerecruiting.me"
        # # Send the message via our own SMTP server.
        # s = smtplib.SMTP('localhost')
        # s.send_message(msg)
        # s.quit()
        return render_template("response.html", name=name, email=email, subject=subject, message=message)
