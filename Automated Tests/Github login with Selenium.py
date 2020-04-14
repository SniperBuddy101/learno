import login_data
from selenium import webdriver

chrome_instance = webdriver.Chrome("/Users/shreyashkarnik/PycharmProjects/Python Project/Automated Tests/chromedriver")

chrome_instance.get("https://github.com")

sign_in = chrome_instance.find_element_by_link_text("Sign in")
sign_in.click()

login_field = chrome_instance.find_element_by_id("login_field")
login_field.send_keys(login_data.user_name)

password_field = chrome_instance.find_element_by_id("password")
password_field.send_keys(login_data.password)

password_field.submit()
header = chrome_instance.find_element_by_class_name("header-nav-current-user")
assert "SniperBuddy101" in header.get_attribute("innerHTML")

print(header.get_attribute("innerHTML"))
print("")
print(chrome_instance.get_cookies())
chrome_instance.quit()
