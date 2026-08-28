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
        self.driver.get(url)
        return self

    def click_at_coordinates(self, x=0, y=0):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        return self

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
            element,
        )
        return self

    def wait_for_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)
        return self

    def attach_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
        return self

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)
        return self

    def get_element_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def focus_element(self, element):
        self.driver.execute_script("arguments[0].focus();", element)
        return self

    def select_text(self, element):
        self.driver.execute_script("arguments[0].select();", element)
        return self
