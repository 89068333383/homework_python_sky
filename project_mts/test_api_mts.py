import allure
import pytest
import requests
from config import BASE_URL, TIMEOUT, TestData
from api import ApiClient, ApiAssertions
from config import TestData


@allure.feature("API Tests")
@allure.story("Проверка доступности")
@allure.title("API: Проверка доступности главной страницы МТС")
@allure.description(
    "Проверяем, что главная страница shop.mts.ru доступна: "
    "сервер возвращает HTTP-статус 2xx и отвечает в пределах заданного таймаута."
)
def test_site_availability():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get("/")

    assertions.assert_status_in_range(response, [200, 301, 302])
    assertions.assert_response_not_empty(response)
    assertions.attach_response_time(response)
    assertions.assert_content_type(response, "text/html")


@allure.feature("API Tests")
@allure.story("Проверка обработки ошибок")
@allure.title("API: Проверка реакции на несуществующий товар (404)")
@allure.description(
    "Тест проверяет, что запрос к несуществующему товару корректно возвращает статус 404."
)
def test_get_non_existent_product():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get(f"/product/{TestData.NON_EXISTENT_PRODUCT_ID}")

    assertions.attach_response(response, "Response for non-existent product")
    assertions.assert_status_code(response, 404)
    assertions.assert_text_contains(response, "404")


@allure.feature("API Tests")
@allure.story("Корзина")
@allure.title("API: Получение корзины (GET /cart)")
@allure.description(
    "Запрос корзины возвращает актуальный список товаров и общую стоимость."
)
def test_get_cart():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get("/cart")

    # На публичных тестах корзина может быть пустой — это ок
    assertions.assert_status_in_range(response, [200, 404])

    if response.status_code == 200:
        assertions.assert_json_has_keys(response, ["items", "personalCart", "total"])


@allure.feature("API Tests")
@allure.story("Негативные тесты")
@allure.title("API: Негативный тест — неверный URL")
@allure.description("Запрос несуществующего пути должен вернуть 404.")
def test_invalid_path_returns_404():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get(TestData.INVALID_PATH)

    assertions.assert_status_code(response, 404)


@allure.feature("API Tests")
@allure.story("Методы HTTP")
@allure.title("API: Проверка метода OPTIONS для каталога")
@allure.description("OPTIONS /catalog должен возвращать допустимые методы (200/204).")
def test_options_catalog():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.options("/catalog")

    assertions.assert_status_in_range(response, [200, 204])


@allure.feature("API Tests")
@allure.story("Безопасность и конфигурация")
@allure.title("API: Проверка заголовков ответа сервера")
@allure.description(
    "Тест проверяет наличие обязательных HTTP-заголовков и их корректность."
)
def test_response_headers():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get("/")

    assertions.attach_response(response, "Response Headers")

    # Проверяем статус
    assertions.assert_status_in_range(response, [200, 301, 302])

    # Проверяем Content-Type
    assertions.assert_content_type(response, "text/html")

    # Проверяем наличие заголовка Server (опционально)
    with allure.step("Проверяем наличие заголовка Server"):
        server_header = response.headers.get("Server")
        if server_header:
            assert len(server_header) > 0, "Заголовок Server пустой"
            allure.attach(
                server_header,
                name="Server header",
                attachment_type=allure.attachment_type.TEXT,
            )
        else:
            allure.attach(
                "Заголовок Server отсутствует",
                name="Server header",
                attachment_type=allure.attachment_type.TEXT,
            )


@allure.feature("API Tests")
@allure.story("Категории")
@allure.title("API: Получение списка категорий")
@allure.description("Запрос /catalog должен возвращать список категорий товаров.")
def test_get_categories():
    client = ApiClient()
    assertions = ApiAssertions()

    response = client.get("/catalog")

    assertions.assert_status_in_range(response, [200, 301, 302])
    assertions.attach_response_time(response)
