import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv


load_dotenv()

PASSWORD = os.environ['GMAIL_APP_PASSWORD']
ADDRESS = os.environ['GMAIL_ADDRESS']


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = ADDRESS
    password = PASSWORD
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['from'], password)
    server.send_message(msg)
    server.quit()
