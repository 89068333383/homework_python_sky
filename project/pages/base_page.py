from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.short_wait = WebDriverWait(driver, 10)
        
    def open(self, url):
        """Открыть URL"""
        self.driver.get(url)
        return self
        
    def click_at_coordinates(self, x=0, y=0):
        """Клик в указанные координаты"""
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        return self
        
    def scroll_to_element(self, element):
        """Скролл до элемента"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
            element
        )
        return self
        
    def wait_for_url_contains(self, text):
        """Ожидание URL с текстом"""
        self.wait.until(lambda d: text in d.current_url)
        return self
        
    def attach_screenshot(self, name):
        """Прикрепить скриншот к Allure"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        return self
        
    def save_screenshot(self, path):
        """Сохранить скриншот"""
        self.driver.save_screenshot(path)
        return self
        
    def get_element_text(self, locator):
        """Получить текст элемента"""
        return self.wait.until(EC.presence_of_element_located(locator)).text
        
    def is_element_present(self, locator):
        """Проверить наличие элемента"""
        return len(self.driver.find_elements(*locator)) > 0
        
    def click_with_js(self, element):
        """Клик через JavaScript"""
        self.driver.execute_script("arguments[0].click();", element)
        return self
        
    def focus_element(self, element):
        """Фокус на элементе через JS"""
        self.driver.execute_script("arguments[0].focus();", element)
        return self
        
    def select_text(self, element):
        """Выделить текст в элементе через JS"""
        self.driver.execute_script("arguments[0].select();", element)
        return self