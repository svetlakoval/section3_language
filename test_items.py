# test_items.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button_present(browser):
    """
    Тест проверяет, что на странице товара присутствует кнопка 'Добавить в корзину'.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Ожидаем, что кнопка станет видимой на странице
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )

    # Проверяем, что элемент действительно найден (не None)
    assert button is not None, "Кнопка 'Добавить в корзину' не найдена на странице товара"