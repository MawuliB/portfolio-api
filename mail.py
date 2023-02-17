import smtplib
from email.mime.text import MIMEText


def send_mail(receiver, username, code, first):
    sender_email = "mawulibadassou5@gmail.com"
    receiver_email = receiver
    password = "zirrihcxonhkcktm"
    link = "https://portfolio-production-aeb7.up.railway.app/" + username

    message = MIMEText(
        first
        + " "
        + link
        + "\n\nShare the link to others for viewing"
        + "\n\n\nUse this code to update the site details - "
        + code
    )
    message["Subject"] = "Congratulations"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def send_specific_email(sender, receiver, title, body):
    sender_email = "mawulibadassou5@gmail.com"
    receiver_email = receiver
    password = "zirrihcxonhkcktm"
    message = MIMEText("Message From: " + sender + "\n\n\n" + body)
    message["Subject"] = title
    message["From"] = sender
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender, receiver_email, message.as_string())
