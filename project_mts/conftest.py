import sys
import os

# Добавляем текущую папку в путь поиска
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
