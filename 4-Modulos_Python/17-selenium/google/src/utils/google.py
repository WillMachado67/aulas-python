from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CAMINHO_PASTA = Path(__file__).parent.parent.parent
CAMINHO_DRIVER = CAMINHO_PASTA / 'bin' / 'chromedriver'


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CAMINHO_DRIVER,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    print(CAMINHO_DRIVER.exists())
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')
    input_element = browser.find_element(By.NAME, 'q')
    input_element.send_keys('The zen of python potugues')
    sleep(3)
    input_element.send_keys(Keys.ENTER)
    sleep(5)
    browser.quit()
