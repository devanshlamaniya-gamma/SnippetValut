import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

FROM_EMAIL = os.getenv("SENDERS_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_mail(to_email: str, subject: str, body: str):

    try:
        msg = EmailMessage()
        msg["From"] = FROM_EMAIL
        msg["To"] = to_email
        msg["subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()
            server.login(FROM_EMAIL, EMAIL_PASSWORD)
            server.send(msg)

    except Exception as e:
        print(e)

    return "sent"
