from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, TestData
import allure


class MainPage(BasePage):
    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, TestData.SEARCH_INPUT)
    FIND_BUTTON = (By.XPATH, TestData.FIND_BUTTON)
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def open_main_page(self):
        """Открыть главную страницу"""
        self.open(BASE_URL)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Главная страница",
            attachment_type=allure.attachment_type.PNG
        )
        return self
        
    def search_product(self, search_term):
        """Выполнить поиск товара"""
        search_input = self.short_wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_input.click()
        search_input.clear()
        search_input.send_keys(search_term)
        
        find_button = self.short_wait.until(EC.element_to_be_clickable(self.FIND_BUTTON))
        find_button.click()
        return self
        
    def close_popups(self):
        """Закрыть всплывающие окна кликом по фону"""
        self.click_at_coordinates(0, 0)
        return self
        
    def search_and_navigate(self, search_term):
        """Поиск и переход к результатам"""
        self.search_product(search_term)
        self.close_popups()
        return self