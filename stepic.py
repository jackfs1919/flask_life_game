from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os

pref = {
    "download.default_directory": os.getcwd(),
    "profile.default_content_setting_values.notifications": 2,
}
options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--ash-no-nudges")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/115.0.0.0 Safari/537.36"
)
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-oopr-debug-crash-dump")
options.add_argument("--disable-low-res-tiling")
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_argument("--no-crash-upload")
options.add_argument("--headless")
options.add_argument("--headless=new")
options.headless = True
options.add_argument("--disable-crash-reporter")
# options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("prefs", pref)
url = "https://parsinger.ru/2.5/sites_selectors/index.html"
symbol = "©"

with webdriver.Chrome(options=options) as driver:

    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "div.copyright>p")
    print(element.tag_name)
    # if element:
    #     # Получаем следующий элемент (предполагается, что именно там хранится секретный код)
    #     secret_element = element.find_element(By.XPATH, './following-sibling::*').text.strip()
        
    #     print(f'Код: {secret_element}')
    # else:
    #     print('Элемент не найден.')
