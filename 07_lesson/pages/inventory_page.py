from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы кнопок «Добавить в корзину»
        self.backpack_btn = (By.NAME, "add-to-cart-sauce-labs-backpack")
        self.shirt_btn = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_btn = (By.NAME, "add-to-cart-sauce-labs-onesie")

        self.cart_container = (By.ID, "shopping_cart_container")
        self.checkout_btn = (By.ID, "checkout")

    def add_items(self):
        # Добавляем товары по очереди, ждём кликабельного состояния
        buttons = [self.backpack_btn, self.shirt_btn, self.onesie_btn]
        for btn_locator in buttons:
            btn = self.wait.until(EC.element_to_be_clickable(btn_locator))
            btn.click()

    def go_to_checkout(self):
        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.cart_container))
        cart_btn.click()
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn))
        checkout_btn.click()
