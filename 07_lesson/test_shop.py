import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    # Если нужно, можно убрать headless, чтобы видеть браузер:
    # options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    # 1. Страница логина
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    # 2. Каталог товаров
    inventory_page = InventoryPage(driver)
    inventory_page.add_items()
    inventory_page.go_to_checkout()

    # 3. Оформление заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info()
    total_cost = checkout_page.get_total_cost()

    assert total_cost == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost}"
