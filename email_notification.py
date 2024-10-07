import smtplib
from email.mime.text import MIMEText

def send_email_notification(article_title, article_description):
    """
    Send an email notification using Mailgun SMTP when a new article is found.
    """
    # Email configuration
    sender = "postmaster@sandbox7e6a662b489b4887b526427a74c2ba24.mailgun.org"
    receiver = "moiznadeem32@gmail.com"
    subject = "New Article Detected!"
    body = f"A new article titled '{article_title}' has been published. Description: {article_description}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Mailgun SMTP configuration
    smtp_server = "smtp.mailgun.org"
    smtp_port = 587
    smtp_user = "postmaster@sandbox7e6a662b489b4887b526427a74c2ba24.mailgun.org"
    smtp_password = "00436f2260385f780f946eb0b22ebf0a-5dcb5e36-9ee5ecec"

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, receiver, msg.as_string())
