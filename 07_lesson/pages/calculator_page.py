from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        # Увеличили таймаут до 60 секунд — калькулятор медленный
        self.wait = WebDriverWait(self.driver, 60)

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value: str):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def enter_expression(self):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            # Ищем span, у которого текст точно равен кнопке (normalize-space убирает лишние пробелы)
            xpath = f'//span[normalize-space()="{button}"]'
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            btn.click()

        # Страховочная пауза после последнего клика
        time.sleep(2)

    def get_result(self) -> str:
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT_VALUE, "15"))
        result_element = self.driver.find_element(*self.RESULT_VALUE)
        return result_element.text
