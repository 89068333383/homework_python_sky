from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    sleep (5)
    assert len(links) == 9, f"Ожидалось 9 ссылок '{len(links)}'"
    print(f"ожидалось 9 ссылок, =: '{len(links)}'")

    for link in links:
        assert link.is_displayed()

    first_text = links[0].text
    assert "1" in first_text, f"В тексте первой ссылки должно быть '1''{first_text}'"
    print(f"Текст первой ссылки: '{first_text}'")

    print("Тест пройден!")

    driver.quit()
test_multiple_elements()