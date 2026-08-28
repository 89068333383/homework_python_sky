# pages/basket_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import TestData
import allure

class BasketPage(BasePage):
    # Локаторы
    QUANTITY_INPUT = (By.NAME, TestData.QUANTITY_INPUT)
    MODAL_LIMIT_TEXT = (By.XPATH, TestData.MODAL_LIMIT_TEXT)
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def verify_basket_page_loaded(self):
        """Проверить загрузку страницы корзины"""
        self.wait_for_url_contains("/personal/basket")
        return self
        
    def verify_product_in_basket(self, keyword):
        """Проверить наличие товара в корзине по тексту"""
        self.short_wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        
        assert keyword.lower() in page_text.lower(), (
            f"❌ Товар '{keyword}' не найден в корзине. Возможно, изменилась верстка или товар не добавился."
        )
        return self
        
    def set_quantity_and_trigger_limit(self, quantity):
        """Установить количество товара и вызвать модальное окно ограничения"""
        qty_input = self.wait.until(EC.presence_of_element_located(self.QUANTITY_INPUT))
        
        # Используем JS для фокуса и выделения
        self.focus_element(qty_input)
        self.select_text(qty_input)
        qty_input.send_keys(quantity)
        
        # Нажимаем Enter для триггера проверки лимита
        qty_input.send_keys(Keys.ENTER)
        
        # Ожидаем модальное окно с ограничением
        self.wait.until(EC.visibility_of_element_located(self.MODAL_LIMIT_TEXT))
        
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Скриншот: Модалка ограничения (кол-во > 2 шт)",
            attachment_type=allure.attachment_type.PNG
        )
        return self
        
    def verify_basket_content(self, keyword):
        """Полная проверка корзины"""
        self.verify_basket_page_loaded()
        self.verify_product_in_basket(keyword)
        return self
        
    def attach_basket_screenshot(self):
        """Скриншот корзины"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Результат: товар в корзине",
            attachment_type=allure.attachment_type.PNG
        )
        return self