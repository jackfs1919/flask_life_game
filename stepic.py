from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем путь к драйверу Chrome
# service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Запускаем браузер
with webdriver.Chrome(options=options) as driver:
    # Переходим на веб-сайт
    driver.get('https://parsinger.ru/2.5/sites_selectors/index.html')
    
    # Ищем элемент <p> с текстом, содержащим символ копирайта
    element = driver.find_element(By.CSS_SELECTOR, 'p:-webkit-matches(:contains("©"))')
    
    if element:
        # Получаем следующий элемент (предполагается, что именно там хранится секретный код)
        secret_element = element.find_element(By.XPATH, './following-sibling::*').text.strip()
        
        print(f'Код: {secret_element}')
    else:
        print('Элемент не найден.')
