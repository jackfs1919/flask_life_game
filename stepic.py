##%%
from time import sleep
from playwright.sync_api import Playwright, sync_playwright
URL = "https://parsinger.ru/selenium/3/3.2.4/index.html"
# M1SS10N-P0SS1BL3


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    def req_resp():
        '''
        вывод на экран результатаов GET и POST запросов к page
        вызывается после page = context.new_page()
        '''
        page.on("request", lambda request: print(">>", request.method, request.url))
        page.on("response", lambda response: print("<<", response.status, response.url))

    req_resp()
    page.goto(URL)
    page.locator("#secret-key-button").click()
    kod = page.locator("#secret-key-button").get_attribute("data")
#     page.locator("#userInput").type(kod)
#     page.locator("#checkBtn").click()
    print(kod)
    sleep(10)
    context.close()
    browser.close()
    exit()


with sync_playwright() as playwright:
    run(playwright)