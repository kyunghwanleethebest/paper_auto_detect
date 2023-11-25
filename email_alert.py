import getpass
import smtplib
from email.message import EmailMessage
import logging
import datetime

def alert_mail(EMAIL_ADDR : str = None, EMAIL_PASSWORD : str = None, author : str = 'Unknown'):
    try:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)


        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

        message = EmailMessage()
        content = f'{author}s new material is detected - {datetime.datetime.now()} '
        message.set_content(content)

        message["Subject"] = f"New Material Alert by {author}"
        message["From"] = EMAIL_ADDR 
        message["To"] = EMAIL_ADDR

        smtp.send_message(message)

        smtp.quit()

        print(f"Success Searching -  {datetime.datetime.now()} ")
    except:
        print(f"Failure -   {datetime.datetime.now()}")

