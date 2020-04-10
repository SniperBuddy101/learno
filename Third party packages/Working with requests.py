import requests

dicto = {"id": 101, "name": "Shreyash"}

headers_obj = {
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"}

requests_obj = requests.get("https://httpbin.org/user-agent", headers=headers_obj)

print(requests_obj.json())
