import smtplib
from email.mime.text import MIMEText
import requests

url = "https://www.google.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        print("\n\t\t\t\t\t\tEmail fetched:\n\n\n",html[:500])
    
    else:
        html = f"""Unable to fetch naked website becasue of some error.. \nhere is the status code which i 
        know you will never understand: {response.status_code}"""
    
except Exception as e:
    html = f"Error: {e}"
    print(html)

sender_email = "shaadalam0207@gmail.com"
receiver_email = "shaadiscaptain@gmail.com"
password = "abmh ntuo imuc tebw"

subject = "Hello"
body = f"here is a cool naked website {html}"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,msg.as_string())
    server.quit
    print("Emial send successfully")
except Exception as e:
    print("error",e)