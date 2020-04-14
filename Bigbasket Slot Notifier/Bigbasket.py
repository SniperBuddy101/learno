import requests
from http.cookies import SimpleCookie
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
import bb_data

message = MIMEMultipart()
message["to"] = bb_data.message_to
message["from"] = "Slot Alert!"
message["subject"] = "Big Basket Slots are Available!"
print("Slot searching started..")
while True:
    print("Loop started..")
    raw_data = bb_data.raw_data
    my_cookie = SimpleCookie(raw_data)
    my_cookie_dict = {}
    for i, m in my_cookie.items():
        my_cookie_dict[i] = m.value

    my_cookie = requests.sessions.cookiejar_from_dict(my_cookie_dict)

    session_obj = requests.Session()

    session_obj.cookies = my_cookie

    headers_obj = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"}
    web_page = session_obj.post("https://www.bigbasket.com/mapi/v3.4.0/get-app-data-dynamic/", headers=headers_obj)

    result_dict = dict(web_page.json())

    slot = result_dict["response"]["addresses"][0]["slot"]

    if slot.lower().find("full") == -1:
        message.attach(MIMEText(slot))
        print("Slots are available!", slot)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp_obj:
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login(user=bb_data.username, password=bb_data.password)
            smtp_obj.send_message(message)
            print("Message sent!")
            break
    sleep(300)

# jar = requests.sessions.RequestsCookieJar()
# for key, value in my_cookie_dict.items():
#     jar.set(key, value)
