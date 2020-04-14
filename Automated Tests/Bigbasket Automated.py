# Bigbasket searching

from selenium import webdriver
import path_to_webdriver

chrome_instance = webdriver.Chrome(path_to_webdriver.path)

chrome_instance.get("https://www.bigbasket.com/")

input_group = chrome_instance.find_element_by_xpath("//div [@class = 'input-group']")

search = chrome_instance.find_element_by_xpath("//div [@class = 'input-group']/input [@id = 'input']")
search.send_keys("Maggi Oats noodles")

button = input_group.find_element_by_tag_name("button")

button.click()
chrome_instance.quit()
