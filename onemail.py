import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email account credentials
EMAIL = 'hriday.has.spam@gmail.com'
# PASSWORD = '$password$'
PASSWORD = 'ekow hslz wtvl ayic'

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Email details
sender_email = EMAIL
receiver_email = 'hridaykharpude@gmail.com'
subject = 'This is a test email'
body = 'I would very much like to assume that this shit is till working!!!!!'

def send_email(sender, receiver, subject, body):
    try:
        # Create a MIMEMultipart object
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Create an SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        
        # Start TLS for security
        server.starttls()
        
        # Log in to the email account
        server.login(sender, PASSWORD)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        
        # Close the SMTP session
        server.quit()
        
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send the email
send_email(sender_email, receiver_email, subject, body)
