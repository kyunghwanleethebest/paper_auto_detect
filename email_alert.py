import getpass
import smtplib
from email.message import EmailMessage
import datetime

def alert_mail(EMAIL_ADDR : str = None, EMAIL_PASSWORD : str = None, articles : dict = {}):
    try:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)


        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

        message = EmailMessage()
        content = f'New Important article title : \n'
        for title, authors in articles.items():
            content+=(title+'\n')
            content+=(', '.join(authors)+'\n\n\n')
        #
        message.set_content(content)

        message["Subject"] = f"New Material is detected - {datetime.datetime.now()}"
        message["From"] = EMAIL_ADDR 
        message["To"] = EMAIL_ADDR

        smtp.send_message(message)

        smtp.quit()

        print(f"Success Send Mail -  {datetime.datetime.now()} ")
    except:
        print(f"Failure Send Mail -   {datetime.datetime.now()}")

