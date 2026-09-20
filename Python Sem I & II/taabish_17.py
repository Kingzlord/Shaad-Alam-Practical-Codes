import smtplib
from email.message import EmailMessage
import urllib

TARGET_URL = "https://example.com"
# Your credentials
EMAIL_ADDRESS = "shaadalam0207@gmail.com"
EMAIL_PASSWORD = "abmh ntuo imuc tebw"  # Use App Password for Gmail

# Create the email
msg = EmailMessage()
msg["Subject"] = "Hello from Python"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "shaadiscaptain@gmail.com"
msg.set_content("Hello there... welcome to this world of python")

# Connect and send
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()                 # Secure the connection
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login first
server.send_message(msg)          # Then send email
server.quit()                     # Close connection

print("Email sent successfully!")
print(f"URL: {TARGET_URL}")
print(f"DOCTYPE: <!{doc_type}>")
print(f"PAGE TITLE: {page_title}")
