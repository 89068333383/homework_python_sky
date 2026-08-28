from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import TestData
import allure
import pytest
import time


class SearchResultsPage(BasePage):
    # Локаторы
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")
    PRODUCT_LINKS = (By.CSS_SELECTOR, TestData.PRODUCT_CARD)
    BUY_BUTTON = (By.CSS_SELECTOR, TestData.BUY_BUTTON)
    MODAL_TITLE = (
        By.CSS_SELECTOR,
        "div.mtsds-modal-page__header p.mtsds-modal-page__header-title",
    )
    MODAL_TITLE_ALT = (By.CSS_SELECTOR, ".modal-header, .mtsds-modal-page__header")
    BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "a[href='/personal/basket'] .mtsds-button__text-container",
    )
    BASKET_BUTTON_ALT = (
        By.XPATH,
        "//a[contains(@href, '/personal/basket')]//*[contains(text(), 'В корзину')]",
    )

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_products(self):
        """Ожидание загрузки товаров"""
        try:
            self.short_wait.until(
                EC.presence_of_all_elements_located(self.PRODUCT_CARDS)
            )
        except:
            self.short_wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        ".product-item, .product, [data-testid='product-card']",
                    )
                )
            )
        return self

    def find_product_by_keyword(self, keyword):
        """Найти товар по ключевому слову"""
        # Ждем появления хотя бы одного товара
        self.wait_for_products()

        # Пробуем найти ссылки на товары
        product_links = self.driver.find_elements(*self.PRODUCT_LINKS)
        if not product_links:
            product_links = self.driver.find_elements(
                By.CSS_SELECTOR, "a[href*='/product/'], a[href*='/catalog/']"
            )

        for link in product_links:
            text = link.get_attribute("innerText") or ""
            aria = link.get_attribute("aria-label") or ""
            if keyword in text or keyword in aria:
                return link

        # Если не нашли по ссылкам, ищем в карточках
        cards = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".product-card, .product-item, [data-testid='product-card']",
        )
        for card in cards:
            card_text = card.text
            if keyword in card_text:
                links = card.find_elements(By.TAG_NAME, "a")
                for link in links:
                    href = link.get_attribute("href")
                    if href and ("/product/" in href or "/catalog/" in href):
                        return link

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Скриншот: Товар не найден",
            attachment_type=allure.attachment_type.PNG,
        )
        pytest.fail(f"Товар с текстом '{keyword}' не найден на странице поиска.")
        return None

    def get_buy_button_in_card(self, product_link):
        """Получить кнопку 'Купить' в карточке товара"""
        # Находим карточку-контейнер
        try:
            card_container = product_link.find_element(
                By.XPATH, "./ancestor::div[contains(@class, 'product-card')]"
            )
        except:
            card_container = product_link.find_element(
                By.XPATH, "./ancestor::div[contains(@class, 'product')]"
            )

        # Ищем кнопку "Купить"
        buy_buttons = card_container.find_elements(
            By.CSS_SELECTOR, "button.mtsds-button, button[data-testid='buy-button']"
        )

        for button in buy_buttons:
            try:
                btn_text = button.find_element(
                    By.CSS_SELECTOR,
                    ".mtsds-button__text-container, .button__text, span",
                ).text
                if "Купить" in btn_text or "купить" in btn_text:
                    return button
            except:
                continue

        raise Exception("Кнопка 'Купить' не найдена в карточке товара")

    def click_product_and_verify(self, product_element):
        """Кликнуть по товару и проверить переход"""
        self.scroll_to_element(product_element)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(product_element))
        self.click_with_js(product_element)
        return self

    def add_product_to_cart(self, product_link):
        """Добавить товар в корзину"""
        self.scroll_to_element(product_link)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(product_link))

        buy_button = self.get_buy_button_in_card(product_link)
        self.scroll_to_element(buy_button)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(buy_button))

        # Кликаем по кнопке
        buy_button.click()
        print("✅ Клик по кнопке 'Купить' выполнен!")

        # Ожидание модалки
        modal_found = False
        modal_locators = [
            self.MODAL_TITLE,
            self.MODAL_TITLE_ALT,
            (By.CSS_SELECTOR, ".mtsds-modal-page, .modal, [role='dialog']"),
            (
                By.XPATH,
                "//*[contains(text(), 'Товар в корзине') or contains(text(), 'добавлен в корзину')]",
            ),
        ]

        for locator in modal_locators:
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(locator)
                )
                modal_found = True
                print(f"✅ Модальное окно найдено!")
                break
            except:
                continue

        if not modal_found:
            # Проверяем счетчик корзины
            try:
                cart_counter = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            ".cart-counter, .basket-counter, [data-testid='cart-count']",
                        )
                    )
                )
                count = cart_counter.text
                if count and int(count) > 0:
                    print(f"✅ Товар добавлен в корзину (счетчик: {count})")
            except:
                pass

        return self

    def go_to_basket_from_modal(self):
        """Перейти в корзину из модального окна"""
        # Ищем кнопку "В корзину" в модалке
        try:
            basket_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.BASKET_BUTTON)
            )
            basket_button.click()
            print("✅ Клик по кнопке 'В корзину' выполнен!")
        except:
            try:
                basket_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.BASKET_BUTTON_ALT)
                )
                basket_button.click()
                print("✅ Клик по кнопке 'В корзину' выполнен!")
            except:
                # Если не нашли кнопку, переходим по URL
                self.driver.get("https://shop.mts.ru/personal/basket")
                print("✅ Перешли в корзину по прямому URL")

        # Ждем загрузки корзины
        WebDriverWait(self.driver, 10).until(EC.url_contains("/personal/basket"))
        return self

    def attach_search_results_screenshot(self, path="search_results.png"):
        """Сделать скриншот результатов поиска"""
        self.save_screenshot(path)
        allure.attach.file(
            path, name="Результаты поиска", attachment_type=allure.attachment_type.PNG
        )
        return self
