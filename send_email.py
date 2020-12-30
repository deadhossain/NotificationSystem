import smtplib
import os
from email.message import EmailMessage
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# Add your email and app password for this to work.
def send_email(subject, body, to):

    message = EmailMessage()
    message.set_content(body)

    # UPDATE THESE LINES TO YOUR INFO
    # user = os.getenv("EMAIL_FROM_NAME")
    # password = os.getenv("EMAIL_PASSWORD")
    # message['From'] = os.getenv("EMAIL_FROM_ADDRESS")

    email_server = "mail.atilimited.net"
    port = 25
    user = "hossain@atilimited.net"
    password = "AtiLtd@1972#"
    message['From'] = "hossain@atilimited.net"
    message['Subject'] = subject
    message['To'] = to

    # Try to log in to server and send email
    try:
        # Send the message via our own SMTP server.
        # server = smtplib.SMTP(os.getenv("EMAIL_SERVER"), os.getenv("PORT"))
        server = smtplib.SMTP(email_server, port)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.send_message(message)
        server.quit()
    except Exception as e:
        # Print any error messages to stdout
        print(e)
        

if __name__ == '__main__':
    send_email("Test","pthone test mail","hossain@atilimited.net")