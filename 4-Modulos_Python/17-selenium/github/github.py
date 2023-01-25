from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

CAMINHO_PASTA = Path(__file__).parent
CAMINHO_DRIVER = CAMINHO_PASTA / 'chromedriver'


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
    browser.get('https://github.com/')
    sleep(2)
    browser.find_element(By.CLASS_NAME, 'Button-content').click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive.header-overlay.home-campaign > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.position-relative.mr-lg-3.d-lg-inline-block > a').click()
    sleep(2)
    input_username = browser.find_element(By.NAME, 'login')
    input_password = browser.find_element(By.NAME, 'password')
    input_username.send_keys(os.getenv('FROM_EMAIL', ''))
    input_password.send_keys(os.getenv('FROM_PASSWORD', ''))
    sleep(1)
    input_password.send_keys(Keys.ENTER)
    sleep(3)
    perfil = browser.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.full-width > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
    print('perfil')
    perfil.click()
    sleep(3)
    go_perfil = browser.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.full-width > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > div.header-nav-current-user.css-truncate > a > strong')
    print('go_perfil')
    go_perfil.click()
    sleep(7)
    go_repositories = browser.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.page-profile.mine > div.application-main > main > div.mt-4.position-sticky.top-0.d-none.d-md-block.color-bg-default.width-full.border-bottom.color-border-muted > div > div > div.Layout-main > div > nav > a:nth-child(2)')
    print('go_repositories')
    go_repositories.click()
    sleep(3)
    go_aula_python = browser.find_element(By.CSS_SELECTOR,'#user-repositories-list > ul > li:nth-child(1) > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a')
    print('go_aula_python')
    go_aula_python.click()
    sleep(5)
    perfil2 = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div[7]/details/summary/img')
    print('perfil2')
    perfil2.click()
    sleep(3)
    sing_out = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/details-menu/form/button')
    print('sing_out')
    sing_out.click()
    sleep(3)
    browser.quit()
