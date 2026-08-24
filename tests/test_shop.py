import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и управления экземпляром браузера Edge.
    
    Настраивает опции браузера, запускает Edge, разворачивает окно на весь экран,
    передаёт драйвер в тест, после завершения теста корректно закрывает браузер.
    
    Yields:
        webdriver.Edge: Экземпляр драйвера Microsoft Edge, готовый к использованию в тестах.
    """
    options = Options()
    # Если нужно, можно убрать headless, чтобы видеть браузер:
    # options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест магазина: полный сценарий покупки")
@allure.description("Проверяет полный сценарий оформления заказа: авторизация, добавление товаров, переход к оформлению, заполнение данных и проверка итоговой суммы (58.29).")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    # 1. Страница логина
    login_page = LoginPage(driver)
    with allure.step("Шаг 1: Открываем страницу логина и авторизуемся"):
        login_page.open()
        login_page.login()

    # 2. Каталог товаров
    inventory_page = InventoryPage(driver)
    with allure.step("Шаг 2: Добавляем товары в корзину и переходим к оформлению"):
        inventory_page.add_items()
        inventory_page.go_to_checkout()

    # 3. Оформление заказа
    checkout_page = CheckoutPage(driver)
    with allure.step("Шаг 3: Заполняем данные покупателя и получаем итоговую сумму"):
        checkout_page.fill_info()
        total_cost = checkout_page.get_total_cost()

    with allure.step("Шаг 4: Проверяем, что итоговая сумма равна 58.29"):
        assert total_cost == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost}"
