from selenium import webdriver
import time
import json
from pprint import pprint

post = {}
driver = webdriver.Firefox()
driver.get("https://mp.weixin.qq.com")
time.sleep(3)
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys("739121527@qq.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("foolish@hungry")
time.sleep(5)
driver.find_element_by_class_name("icon_checkbox").click()
driver.find_element_by_class_name("btn_login").click()
time.sleep(20)
driver.get("https://mp.weixin.qq.com")
cookie_items = driver.get_cookies()
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with open('cookie.txt', 'w+', encoding='utf-8') as f:
    f.write(cookie_str)
