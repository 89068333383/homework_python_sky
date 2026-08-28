from pages.base_page import BasePage
import allure


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def verify_product_page_loaded(self):
        """Проверить загрузку страницы товара"""
        self.wait_for_url_contains("/product/")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Страница карточки товара",
            attachment_type=allure.attachment_type.PNG
        )
        return self