import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL = 'hriday.has.spam@gmail.com'
PASSWORD = 'ekow hslz wtvl ayic'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
subject = 'This is a test email'

csv_file_path = 'data.csv'

def send_email(sender, receiver, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender, PASSWORD)
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        server.quit()
        
        print(f"Email sent successfully to {receiver}")
    except Exception as e:
        print(f"Failed to send email to {receiver}: {e}")

def send_bulk_emails(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            receiver_email = row['email']
            name = row['name']
            body = f"Hello {name},\n\nI would very much like to assume that this email is still working!!!!!"
            send_email(EMAIL, receiver_email, subject, body)



send_bulk_emails(csv_file_path)
