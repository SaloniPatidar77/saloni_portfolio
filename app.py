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
        gmail_email = os.environ.get("GMAIL_EMAIL")
        gmail_password = os.environ.get("GMAIL_APP_PASSWORD")

        if not gmail_email or not gmail_password:
            return "Email configuration is missing.", 500

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            timeout=20
        ) as smtp:

            smtp.login(
                gmail_email,
                gmail_password
            )

            smtp.send_message(msg)

        return render_template("success.html")

    except Exception as e:
        print("EMAIL ERROR:", e)
        return "Unable to send your message right now. Please try again later.", 500


if __name__ == "__main__":
    app.run(debug=True)