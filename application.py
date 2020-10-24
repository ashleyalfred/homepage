from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

def send_email(name, email, subject, message):
    mailgun_domain = os.environ.get('MAILGUN_DOMAIN')
    return requests.post(
        f'https://api.mailgun.net/v3/{mailgun_domain}/messages',
        auth=("api", os.environ.get('MAILGUN_API_KEY')),
        data={
            'from': 'Homepage <mailgun@sandbox.mgsend.net>',
            'to': [os.environ.get('CONTACT_EMAIL_ADDR')],
            'subject': subject,
            'text': f'From: {name} <{email}>\n\n{message}'
        }
    )

def save_contact(name, email, subject, message):
    import sqlite3
    conn = sqlite3.connect('website.db')
    c = conn.cursor() 
    c.execute("INSERT into registrants (name, email, subject, message) VALUES (?, ?, ?, ?)", (name, email, subject, message))
    conn.commit()
    conn.close()

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
        # save_contact(name, email, subject, message)
        send_email(name, email, subject, message)
        return render_template("response.html", name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)