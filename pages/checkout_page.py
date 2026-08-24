from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Страница оформления заказа.
    Предоставляет методы для заполнения данных и подтверждения заказа.
    """
    def __init__(self, driver):
        """
        Инициализирует страницу оформления заказа.
        Args:
            driver (selenium.webdriver): Экземпляр драйвера браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
# Подставь свои локаторы
        self.first_name_input = (By.CSS_SELECTOR, "#first-name")
        self.last_name_input = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_input = (By.CSS_SELECTOR, "#postal-code")
        self.continue_btn = (By.CSS_SELECTOR, "#continue")

        self.total_cost_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name="Oxana", last_name="Kl", postal_code="450000"):
        """
        Заполняет форму данных покупателя.
        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            zip_code (str): Почтовый индекс.
        Returns:
            None
        """
        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.first_name_input))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_field = self.driver.find_element(*self.postal_code_input)
        postal_field.clear()
        postal_field.send_keys(postal_code)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.continue_btn))
        continue_btn.click()

    def get_total_cost(self) -> float:
        total_label = self.wait.until(
            EC.visibility_of_element_located(self.total_cost_label))
        text = total_label.text  # например, "Total: $58.29"
        # Убираем "Total: $" и преобразуем в float
        value_str = text.replace("Total: $", "").strip()
        return float(value_str)
