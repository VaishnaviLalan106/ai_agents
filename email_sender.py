import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,app_password

# Email details
def send_email(receiver_email: str, subject: str, content: str) -> str:
    """Send an email to the receiver with the given subject and content."""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    return f"Email sent successfully to {receiver_email}!"
