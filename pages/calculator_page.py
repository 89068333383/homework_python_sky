from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:
    """
    Страница калькулятора.
    Предоставляет методы для ввода чисел, выбора операций и получения результата.
    """

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        """
        Инициализирует страницу калькулятора.
        Args:
            driver (selenium.webdriver): Экземпляр драйвера браузера.
            url (str): URL страницы калькулятора.
        """
        self.driver = driver
        self.url = url
        # Увеличили таймаут до 60 секунд — калькулятор медленный
        self.wait = WebDriverWait(self.driver, 60)

    def open(self) -> None:
        """
        Открывает страницу калькулятора по сохранённому URL.

        Returns:
            None
        """
        self.driver.get(self.url)

    def set_delay(self, delay_value: str) -> None:
        """
        Устанавливает значение задержки в поле ввода.

        Args:
            delay_value (str): Значение задержки (в секундах), передаётся как строка.

        Returns:
            None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def enter_expression(self) -> None:
        """
        Вводит выражение «7+8=» нажатием соответствующих кнопок на калькуляторе.

        Returns:
            None
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            # Ищем span, у которого текст точно равен кнопке (normalize-space убирает лишние пробелы)
            xpath = f'//span[normalize-space()="{button}"]'
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            btn.click()

       # Вместо time.sleep(2) ждём появления результата «15» на экране
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT_VALUE, "15"))

    def get_result(self) -> str:
        """
        Получает текущий результат вычисления с экрана калькулятора.
        Перед чтением ждёт появления ожидаемого значения «15» в элементе.

        Returns:
            str: Текст результата, отображаемого на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT_VALUE, "15"))
        result_element = self.driver.find_element(*self.RESULT_VALUE)
        return result_element.text
