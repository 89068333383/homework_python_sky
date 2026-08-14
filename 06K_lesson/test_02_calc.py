from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_input.clear()
    text_input.send_keys("25")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
    )
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"

    driver.quit()
