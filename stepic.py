##%%
from time import sleep
from playwright.sync_api import Playwright, sync_playwright
URL = "https://parsinger.ru/selenium/3/3.3.3/index.html"


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

    # req_resp()
    page.goto(URL)
    # page.locator("#secret-key-button").click()
    par = page.locator("a").all()
    colvo = 0
    for i in par:
        attr = i.get_attribute("stormtrooper")
        if attr.isdigit():
            colvo += int(attr)
    page.locator("#inputNumber").click()
    page.locator("#inputNumber").type(str(colvo))
    page.locator("#feedbackMessage").click()
    # par.locator(".child_class").first.click()
    print(page.locator("#feedbackMessage").text_content())
    sleep(10)
    # context.close()
    browser.close()
    exit()


with sync_playwright() as playwright:
    run(playwright)