import smtplib, ssl

def send_email():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "atilimitedgp@gmail.com"
    receivers = ['hossain@atilimited.net']
    password = "Ati@1234"

    # Create a secure SSL context
    context = ssl.create_default_context()

    message = """From: atilimitedgp@gmail.com
    To: hossain@atilimited.net
    MIME-Version: 1.0
    Content-type: text/html
    Subject: Python Test Mail

    This is an e-mail message to be sent in HTML format

    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
    """

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receivers, message)   
        print("Successfully sent email")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()