import smtplib
from email.mime.text import MIMEText
import requests

url = "https://www.google.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text[:500]   # first 500 chars
        print("Fetched HTML:\n")
        print(html)
    else:
        html = f"Failed to fetch page. Status code: {response.status_code}"
        print(html)

except Exception as e:
    html = f"Error: {e}"
    print(html)

sender_email = "shaadalam0207@gmail.com"
receiver_email = "shaadiscaptain@gmail.com"
password = "abmh ntuo imuc tebw"   # NOT your normal password

subject = "Website HTML Output"
body = f"Hello how are you my friend"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("\n✅ Email sent successfully!")

except Exception as e:
    print("\n❌ Failed to send email:", e)