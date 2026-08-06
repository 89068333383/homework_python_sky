from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    driver.maximize_window()

    name_field = driver.find_element(By.NAME, "custname")
    sleep(2)
    name_field.send_keys("Оксана")
    sleep(2)
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()
    assert driver.current_url.endswith("/forms/post"), f"URL не совпал: {driver.current_url}"
    print(driver.current_url)   
    driver.quit()
test_form_submission()


