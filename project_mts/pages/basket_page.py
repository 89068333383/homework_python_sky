from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import TestData
import allure


class BasketPage(BasePage):
    # Локаторы - используем ТОЧНО такие же как в рабочем тесте
    QUANTITY_INPUT = (By.NAME, "input-quantity")  # ТОЧНО такой же как в оригинале
    MODAL_LIMIT_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'dialog-modal__confirm-text') and contains(text(), 'юридическое лицо')]",
    )
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-item, .basket-empty, .empty-basket")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_basket_page_loaded(self):
        """Проверить загрузку страницы корзины"""
        self.wait.until(EC.url_contains("/personal/basket"))
        return self

    def wait_for_basket_to_load(self):
        """Ожидание загрузки корзины"""
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".basket-item, .basket-empty, .empty-basket")
                )
            )
        except:
            pass
        return self

    def verify_product_in_basket(self, keyword):
        """Проверить наличие товара в корзине по тексту"""
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        page_text = self.driver.find_element(By.TAG_NAME, "body").text

        assert (
            keyword.lower() in page_text.lower()
        ), f"❌ Товар '{keyword}' не найден в корзине."

        print(f"✅ Товар '{keyword}' найден в корзине!")
        return self

    def set_quantity_and_trigger_limit(self, quantity):
        """Установить количество товара и вызвать модальное окно ограничения"""
        # ТОЧНО ТАК ЖЕ как в оригинальном работающем тесте

        # Ждём, пока поле появится (но НЕ кликаем по нему!)
        qty_input = self.wait.until(EC.presence_of_element_located(self.QUANTITY_INPUT))

        # ВАЖНО: используем JS для фокуса и выделения (как в оригинале)
        # Это обходит любые оверлеи, которые перехватывают обычный клик
        self.driver.execute_script("arguments[0].focus();", qty_input)
        self.driver.execute_script(
            "arguments[0].select();", qty_input
        )  # Выделяет весь текст

        # Теперь просто отправляем цифру — она заменит выделенное
        qty_input.send_keys(quantity)
        print(f"✅ Ввели количество: {quantity} (через JS focus/select)")

        # Нажимаем Enter, чтобы триггернуть проверку лимита (>2 шт)
        qty_input.send_keys(Keys.ENTER)
        print("✅ Нажали Enter — ждём модальное окно...")

        # Ищем текст модалки: «Хотите продолжить как юридическое лицо?»
        self.wait.until(EC.visibility_of_element_located(self.MODAL_LIMIT_TEXT))
        print("✅ Модальное окно с ограничением найдено — тест достиг цели!")

        # Делаем финальный скриншот именно этой модалки для отчёта
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Скриншот: Модалка ограничения (кол-во > 2 шт)",
            attachment_type=allure.attachment_type.PNG,
        )
        return self

    def verify_basket_content(self, keyword):
        """Полная проверка корзины"""
        self.verify_basket_page_loaded()
        self.wait_for_basket_to_load()
        self.verify_product_in_basket(keyword)
        return self

    def attach_basket_screenshot(self):
        """Скриншот корзины"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Результат: товар в корзине",
            attachment_type=allure.attachment_type.PNG,
        )
        return self
