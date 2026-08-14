from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = [
        ("first-name", "Иван"),
        ("last-name", "Петров"),
        ("address", "Ленина, 55-3"),
        ("city", "Москва"),
        ("country", "Россия"),
        ("e-mail", "test@skypro.com"),
        ("phone", "+7985899998787"),
        ("job-position", "QA"),
        ("company", "SkyPro"),
    ]

    # Заполняем все поля в цикле
    for name, value in fields:
        element = wait.until(EC.presence_of_element_located((By.NAME, name)))
        element.send_keys(value)

    # Нажимаем кнопку Submit
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'], button"))
    )
    submit_button.click()

    zip_code_field = driver.find_element(By.ID, "zip-code")
    color_zip_code = zip_code_field.value_of_css_property("border-color")
    assert color_zip_code == "rgb(245, 194, 199)" in color_zip_code

    fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company",
    ]

    for field_id in fields:
        field_element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
        border_color = field_element.value_of_css_property("border-color")
        assert border_color == "rgb(186, 219, 204)", f"Поле {field_id}"

    driver.quit()
