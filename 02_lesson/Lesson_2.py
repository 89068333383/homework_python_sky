from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()

# Открыть страницу авторизации: https://httpbin.qa-territory.online
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()
   

# Найти и кликнуть на ссылку HTML Form.
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
   

# Проверка URL
    assert driver.current_url.endswith("/forms/post"), f"URL не совпал: {driver.current_url}"
    print(driver.current_url)

#назад
    driver.back()
# ghjdthrf 
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    print(driver.current_url)

    driver.quit()

test_navigation()