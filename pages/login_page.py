from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Страница авторизации в интернет-магазине.
    Содержит методы для открытия страницы и ввода учетных данных.
    """

    def __init__(self, driver):
        """
        Инициализирует страницу.
        Args:
            driver (selenium.webdriver): Экземпляр драйвера браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы элементов
        self.user_name_input = (By.CSS_SELECTOR, "#user-name")
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self, url: str = "http://www.saucedemo.com/") -> None:
        """
        Открывает указанную страницу в браузере.
        Args:
            url (str): Адрес страницы для перехода. По умолчанию — главная страница магазина.
        Returns:
            None
        """
        self.driver.get(url)

    def login(self, username: str = "standard_user", password: str = "secret_sauce") -> None:
        """
        Выполняет вход в систему с указанными учетными данными.
        Args:
            username (str): Логин пользователя.
            password (str): Пароль пользователя.
        Returns:
            None
        """
        # Ввод логина
        user_field = self.wait.until(
            EC.visibility_of_element_located(self.user_name_input))
        user_field.clear()
        user_field.send_keys(username)

        # Ввод пароля
        pass_field = self.driver.find_element(*self.password_input)
        pass_field.clear()
        pass_field.send_keys(password)

        # Нажатие кнопки входа
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
