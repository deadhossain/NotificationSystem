import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(subject, body, to):
    from_email_address="hossain@atilimited.net"
    me_password="AtiLtd@1972#"   # Put YOUR password here
    to_email_addresses=to
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email_address
    msg['To'] = ','.join(to_email_addresses)
    msg.preamble = subject
    msg_txt = ("<html>"
                "<head></head>"
                "<body>"
                    "<h1>%s</h1>"
                "</body>"
            "</html>" % body)

    msg.attach(MIMEText(msg_txt, 'html'))
    smtp_conn = smtplib.SMTP("mail.atilimited.net", 587,timeout=10)
    # print ("connection stablished")
    smtp_conn.starttls()
    smtp_conn.ehlo_or_helo_if_needed()
    smtp_conn.login(from_email_address, me_password)
    smtp_conn.sendmail(from_email_address, to_email_addresses, msg.as_string())
    smtp_conn.quit()

if __name__ == "__main__":
    send_mail("Test","pthone test mail","hossain@atilimited.net")