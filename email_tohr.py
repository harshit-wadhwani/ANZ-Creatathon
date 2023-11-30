import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_to_hr(candidate_email,name, score, questions, answers, phone):
    # Email configuration
    sender_email = 'sejalkaur.work@gmail.com'  # sender email address
    password = 'vakv rmbu copp fakk'  # sender email password
    hr_email = 'harshitwadhwani23@gmail.com'  # HR's email address
    subject = 'New Candidate Submission'

    # Build the email body with questions
    message = f'Dear HR,\n\nA new candidate has submitted their application. Details are as follows:\n\nCandidate Name: {name}\n\nCandidate Email: {candidate_email}Candidate Phone Number: {phone}\n\n\n\nPlease find below the interview questions:\n\n'
    message += '\n'.join(questions)
    message += '\n\nAnswers:\n'
    message += '\n'.join(answers)
    message += "\n\nScore: " + str(score)
    message += "\n\nBest regards,\n Team ctrl+shift+esc"

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
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail SMTP server and port 587
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent to HR successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_email_to_hr('sejalkaur.work@gmail.com', 33, ['test'], ['test'], '779000')
