##%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

# Запустим браузер
browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/9/9.4.2/index.html"
browser.delete_all_cookies()
browser.get(url)

# Нажимаем кнопку START
start_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='START']"))
)
start_button.click()

# Переменная для суммы чисел
total_sum = 0
num = 1
try:
    while True:
        # Ждем смены URL страницы
        previous_url = browser.current_url
        WebDriverWait(browser, 5).until(EC.url_changes(previous_url))
        
        # Получаем текущий URL
        current_url = browser.current_url
        # browser.save_screenshot(f'scr{num}.png')
        # num += 1
        # Проверяем, соответствует ли URL нужному паттерну
        if re.match(r'^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$', current_url):
            # Считываем число с текущей страницы
            number_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "number"))
            )
            number = int(number_element.text)
            total_sum += number
        
        # Проверяем, не открылась ли финальная страница
        if "index2" in current_url:
            break

except Exception as e:
    print(f"Произошла ошибка: {e}")

# Вводим сумму на финальной странице
# input_field = WebDriverWait(browser, 10).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='number']")))
input_f = browser.find_element(By.XPATH, "//input")
# input_field.send_keys(total_sum)
input_f.click()
time.sleep(1)
total_sum = 542364
input_f.send_keys(total_sum)

# Нажимаем кнопку Проверить
# check_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Проверить']")))
check_button = browser.find_element(By.XPATH, "//button")

# time.sleep(1)
check_button.click()

print(total_sum)
time.sleep(1000)
# Получаем пароль
password_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "password"))
)
password = password_element.text
print(f"Полученный пароль: {password}")

# Закрываем браузер
browser.quit()


