import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и управления экземпляром браузера Chrome.
    
    Yields:
        webdriver.Chrome: Экземпляр драйвера Chrome, готовый к использованию в тестах.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора: проверка результата с задержкой")
@allure.description("Проверяет работу медленного калькулятора: устанавливается задержка 45 сек, вводится выражение, проверяется результат 15.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)

    with allure.step("Шаг 1: Открываем страницу медленного калькулятора"):
        calc_page.open()

    with allure.step("Шаг 2: Устанавливаем задержку 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Шаг 3: Вводим выражение в калькулятор"):
        calc_page.enter_expression()

    with allure.step("Шаг 4: Получаем результат вычисления"):
        result = calc_page.get_result()

    with allure.step("Шаг 5: Проверяем, что результат равен 15"):
        assert result == "15"