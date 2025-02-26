##%%
from time import sleep
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = "http://parsinger.ru/selenium/9/9.3.1/index.html"
browser = webdriver.Chrome()
browser.get(URL)
# iframe = browser.find_element('tag name', 'iframe')
# browser.switch_to.frame(iframe)
# text = browser.page_source
# words = ''.join(re.findall(r'\*(.*?)\*', text))
# print(words)
sleep(200)
total_likes = 0


print(total_likes)

browser.quit()
os.system("taskkill /im chrome.exe /f")
