import time
from selenium.webdriver.common.by import By


def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    message = 'Кнопка добавления товара в корзину отсутсвует'
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket').is_displayed(), message

