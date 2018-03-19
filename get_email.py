# from selenium import webdriver
# import re
# driver=webdriver.Chrome('/Users/Tiernan/Desktop/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.get('http://home.baidu.com/contact.html')
# doc=driver.page_source#获取源代码
# emails=re.findall(r'[\w]+@[\w\.-]+',doc)
# for email in emails:
#     print(email)

# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/Tiernan/Desktop/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.get_screenshot_as_file("/Users/Tiernan/Desktop/baidu.png")
driver.quit()