# print("\n"*30)
import urllib.request
from bs4 import BeautifulSoup

TARGET_URL = "https://example.com"

def get_doctype_and_content(url):
    try:
        # 1. Open the URL using urllib
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            html_data = response.read()

        # 2. Parse with BeautifulSoup
        soup = BeautifulSoup(html_data, 'html.parser')

        # 3. Find the DOCTYPE
        # BeautifulSoup stores the DOCTYPE in the 'contents' list as a special object
        doctype = [item for item in soup.contents if isinstance(item, str) == False][0]
        
        return doctype, soup.title.string
    except Exception as e:
        return None, f"Error: {e}"

# --- EXECUTION ---
doc_type, page_title = get_doctype_and_content(TARGET_URL)

print(f"URL: {TARGET_URL}")
print(f"DOCTYPE: <!{doc_type}>")
print(f"PAGE TITLE: {page_title}")


import smtplib
from email.message import EmailMessage

# --- 1. SETUP YOUR DETAILS ---
EMAIL_ADDRESS = "shaadalam0207@gmail.com"
EMAIL_PASSWORD = "dwqp xnqc zqgn vbem"  # Your Gmail App Password
RECEIVER_EMAIL = "shaadalam0207@gmail.com"

# --- 2. GET THE URL ---
# This makes the script wait for you to paste the link
target_url = input("Paste the URL you want to share: ")

# --- 3. CREATE THE MESSAGE ---
msg = EmailMessage()
msg["Subject"] = "Thinking of you!"
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECEIVER_EMAIL

# Here is your simple message combined with the link
content = f"How are you doing?\n\nI found this link and thought of you:\n{target_url}"
msg.set_content(content)

# --- 4. SEND THE EMAIL ---
try:
    # Using Port 465 for a secure SSL connection
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Successfully sent the link!")
except Exception as e:
    print(f"Something went wrong: {e}")

