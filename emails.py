import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(candidate_email):
    # Email configuration
    sender_email = 'your_email@example.com'  # sender email address
    password = 'your_password'  # sender email password
    subject = 'Thank you for your submission'
    message = 'Dear Candidate, \n\nThank you for submitting your application. Our system shall review it carefully and revert to you within 1 working day.\n\nBest regards,\n Team automatic'
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")