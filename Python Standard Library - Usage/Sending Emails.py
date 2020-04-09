from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

text_msg = MIMEText("""

Sent with SSL

""")
img_rqrd = MIMEImage(Path("imagefile.png").read_bytes())

message = MIMEMultipart()
message["to"] = "receiver@gmail.com"
message["from"] = "Shehenshah Shreyash"
message["subject"] = "Swagat Nahi Karoge Humara?"
message.attach(text_msg)
message.attach(img_rqrd)

with smtplib.SMTP_SSL(host="smtp.gmail.com") as smtp_obj:
    smtp_obj.ehlo()
    smtp_obj.login(user="sender@bajiraobhayankar.com", password="thepassword")
    smtp_obj.send_message(message)

print("Message sent!")
