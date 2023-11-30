import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_to_hr(candidate_email, score, questions, answers, phone):
    # Email configuration
    sender_email = 'sejalkaur.work@gmail.com'  # sender email address
    password = 'Jupy1298'  # sender email password
    hr_email = 'harshitwadhwani23@gmail.com'  # HR's email address
    subject = 'New Candidate Submission'

    # Build the email body with questions
    message = f'Dear HR,\n\nA new candidate has submitted their application. Details are as follows:\n\nCandidate Email: {candidate_email}\n\nPlease find below the interview questions:\n\n'
    message += '\n'.join(questions)
    message +=  '\n'.join(answers)
    message += "\n" + score
    message += '\n\nBest regards,\n Team automatic'
    
    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = hr_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Attach candidate's resume
    resume_path = os.path.join('uploads', f'{candidate_email}.pdf')
    with open(resume_path, 'rb') as resume_file:
        resume_attachment = MIMEApplication(resume_file.read(), Name=os.path.basename(resume_path))
    resume_attachment['Content-Disposition'] = f'attachment; filename={os.path.basename(resume_path)}'
    msg.attach(resume_attachment)

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent to HR successfully!")
    except Exception as e:
        print(f"Error: {e}")
