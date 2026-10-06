from flask import Flask, render_template, request
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    msg = EmailMessage()

    msg["Subject"] = f"Portfolio Contact: {subject or 'New Message'}"
    msg["From"] = os.environ.get("GMAIL_EMAIL")
    msg["To"] = os.environ.get("GMAIL_EMAIL")
    msg["Reply-To"] = email

    msg.set_content(
        f"""New message from your portfolio

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                os.environ.get("GMAIL_EMAIL"),
                os.environ.get("GMAIL_APP_PASSWORD")
            )
            smtp.send_message(msg)

        return render_template("success.html")

    except Exception:
        return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)