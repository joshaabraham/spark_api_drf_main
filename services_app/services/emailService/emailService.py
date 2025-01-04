import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to):
    sender_email = os.getenv("EMAIL_HOST_USER")
    sender_password = os.getenv("EMAIL_HOST_PASSWORD")

    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error while sending email: {e}")