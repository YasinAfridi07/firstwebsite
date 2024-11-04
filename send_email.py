import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def handler(request):
    # Parse the form data
    form_data = request.form
    name = form_data.get("name")
    email = form_data.get("email")
    message = form_data.get("message")

    # Set up email content
    recipient_email = "yasinusman222@gmail.com"  # Your email where submissions will be sent
    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    # Email configuration
    smtp_server = "smtp.gmail.com"  # Change to Gmail's SMTP server
    smtp_port = 465  # Use 587 for TLS, or 465 for SSL
    smtp_user = os.getenv("yasinusman222@gmail.com")  # Your Gmail address
    smtp_pass = os.getenv("drct rqfa viir sutz")  # Your app-specific password

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection for port 587
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, recipient_email, msg.as_string())
        return {
            "statusCode": 200,
            "body": "Thank you for contacting us!"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Failed to send email: {str(e)}"
        }
