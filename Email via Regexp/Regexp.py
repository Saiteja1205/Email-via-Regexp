import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    name = input("Enter Name: ")
    if pattern.fullmatch(name):
        break
    else:
        print("Enter Name in correct format (only letters and spaces).")

while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    if pattern.fullmatch(dob):
        break
    else:
        print("Enter DOB in correct format (DD-MM-YYYY).")
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone = input("Enter Mobile Number (XXX-XXX-XXXX): ")
    if pattern.fullmatch(phone):
        break
    else:
        print("Enter Mobile Number in correct format (XXX-XXX-XXXX).")

while True:
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    email = input("Enter Email: ")
    if pattern.fullmatch(email):
        break
    else:
        print("Enter Email in correct format (example@gmail.com).")

insta = input("Enter Insta ID: ")

print("\nAll details verified successfully!\n")


sender_email = "chunku.saiteja03@gmail.com" 
sender_password = "aeyo nfyj znkh vaxz"  

subject = "Registration Successful"
body = f"""
Hello {name},

Thank you for registering with us!

Here are your details:
- Name: {name}
- Date of Birth: {dob}
- Mobile: {phone}
- Instagram ID: {insta}
- Email: {email}

If this wasn't you, please ignore this email.

Regards,  
Your Team
"""

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()
    print("Email sent successfully to", email)
except Exception as e:
    print("Error sending email:", e)
