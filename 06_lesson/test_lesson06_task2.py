from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://gitflic.ru/.
    driver.get("https://www.gitflic.ru/")
    # 2. Установите cookie пользователя 1.
    # ogjxvntplllsdwg-76989@ai.24.email
    # User12345$

    oxana_k = driver.add_cookie(
        {
            "name": "SESSION",
            "value": "MjFjYTg0NTctZDNkZS00NzNkLThhYWYtNTBhZWUwZWZlODM3",
            "domain": "gitflic.ru",
        }
    )

    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    driver.refresh()

    driver.maximize_window()
    driver.get("https://gitflic.ru/user/oxana_k")

    oxana_k = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()

    a89068333383 = driver.add_cookie(
        {
            "name": "SESSION",
            "value": "2YwNzA4ZTEtNTVmNC00MTgyLTg3NWUtZDdiOTRhYzE2ZTNj",
            "domain": "gitflic.ru",
        }
    )

    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    driver.refresh()

    driver.get("https://gitflic.ru/user/a89068333383")

    a89068333383 = driver.current_url

    assert oxana_k != a89068333383

    driver.quit()


test_session_storage_auth()
