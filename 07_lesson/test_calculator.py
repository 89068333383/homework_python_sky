import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)

    calc_page.open()
    calc_page.set_delay("45")
    calc_page.enter_expression()

    result = calc_page.get_result()
    assert result == "15"
