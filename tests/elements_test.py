import time
from pages.base_page import BasePage

def test(driver):
    page = BasePage(driver, 'https://www.ya.ru')
    page.open()
    time.sleep(2)