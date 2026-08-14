from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div#start button"))
    )
    start_button.click()
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#finish h4"), "Hello World!"
        )
    )
    finish = driver.find_element(By.ID, "finish")

    screenshot_path = "debug_screenshot.png"
    driver.save_screenshot(screenshot_path)

    assert finish.text == "Hello World!"
    driver.quit()


test_dynamic_loading()
