import smtplib
from email.mime.text import MIMEText


def send_mail(receiver, username):
    sender_email = "mawulibadassou5@gmail.com"
    receiver_email = receiver
    password = "zirrihcxonhkcktm"
    link = "http://localhost:3000/" + username

    message = MIMEText(
        "Your Site is ready for viewing at "
        + link
        + "\n\nShare the link to others for viewing"
    )
    message["Subject"] = "Congratulations"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
