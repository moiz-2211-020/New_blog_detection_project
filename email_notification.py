import smtplib
from email.mime.text import MIMEText

def send_email_notification(article_title, article_url):
    """
    Send an email notification when a new article is found.
    """
    # Email configuration
    sender = "moiz.khan.edu15@gmail.com"
    receiver = "moiznadeem32@gmail.com"
    subject = "New Article Detected!"
    body = f"A new article titled '{article_title}' has been published. Read it here: {article_url}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender, "your-password")
        server.sendmail(sender, receiver, msg.as_string())
