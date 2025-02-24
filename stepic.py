##%%
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/7/7.5/index.html"
driver = webdriver.Chrome()
driver.get(URL)
sleep(5)
total_likes = 0
actions = ActionChains(driver)
div = driver.find_element('id', 'container')
for _ in range(30):
    actions.pause(1) \
        .key_down(Keys.END, div) \
        .perform()
sleep(3)
cards = driver.find_elements('class name', 'card')
actions.pause(1) \
    .key_down(Keys.HOME, div) \
    .perform()
sleep(3)
for card in cards:
    card.find_element('class name', 'like-btn').click()
    sleep(1)
    total_likes += int(card.find_element('class name', 'big-number').text)
    actions.key_down(Keys.ARROW_DOWN, div)

print(total_likes)

driver.quit()
os.system("taskkill /im chrome.exe /f")
