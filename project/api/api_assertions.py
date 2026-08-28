import allure
import json


class ApiAssertions:
    """Класс с проверками для API ответов"""
    
    @staticmethod
    def assert_status_code(response, expected_status):
        """Проверить статус код"""
        with allure.step(f"Проверяем статус-код: ожидается {expected_status}"):
            assert response.status_code == expected_status, \
                f"Ожидался статус {expected_status}, получен {response.status_code}"
        return response
        
    @staticmethod
    def assert_status_in_range(response, status_codes):
        """Проверить, что статус код входит в список допустимых"""
        with allure.step(f"Проверяем статус-код: ожидается один из {status_codes}"):
            assert response.status_code in status_codes, \
                f"Ожидался один из статусов {status_codes}, получен {response.status_code}"
        return response
        
    @staticmethod
    def assert_response_not_empty(response):
        """Проверить, что ответ не пустой"""
        with allure.step("Проверяем, что ответ не пустой"):
            assert len(response.content) > 0, "Ответ сервера пустой"
        return response
        
    @staticmethod
    def assert_content_type(response, expected_type="text/html"):
        """Проверить Content-Type заголовок"""
        with allure.step(f"Проверяем Content-Type: ожидается {expected_type}"):
            content_type = response.headers.get("Content-Type", "")
            assert content_type != "", "Заголовок Content-Type отсутствует"
            assert expected_type in content_type.lower(), \
                f"Неверный Content-Type. Ожидался {expected_type}, получен: {content_type}"
        return response
        
    @staticmethod
    def assert_header_present(response, header_name):
        """Проверить наличие заголовка"""
        with allure.step(f"Проверяем наличие заголовка '{header_name}'"):
            assert header_name in response.headers, f"Заголовок '{header_name}' отсутствует"
        return response
        
    @staticmethod
    def assert_json_has_keys(response, keys):
        """Проверить наличие ключей в JSON ответе"""
        with allure.step(f"Проверяем наличие ключей в JSON: {keys}"):
            try:
                data = response.json()
                for key in keys:
                    if key not in data:
                        # Если точного совпадения нет, проверяем частичное совпадение
                        found = False
                        for data_key in data.keys():
                            if key.lower() in data_key.lower() or data_key.lower() in key.lower():
                                found = True
                                break
                        assert found, f"Ключ '{key}' или его аналог отсутствует в ответе"
            except json.JSONDecodeError:
                # Если ответ не JSON, проверяем наличие текста
                assert any(key.lower() in response.text.lower() for key in keys), \
                    f"Ни один из ключей {keys} не найден в ответе"
        return response
        
    @staticmethod
    def assert_text_contains(response, text):
        """Проверить, что текст ответа содержит указанную строку"""
        with allure.step(f"Проверяем наличие текста '{text}' в ответе"):
            assert text in response.text or text.lower() in response.text.lower(), \
                f"Текст '{text}' не найден в ответе"
        return response
        
    @staticmethod
    def attach_response_time(response):
        """Прикрепить время ответа к Allure"""
        with allure.step("Фиксируем время ответа"):
            response_time_ms = int(response.elapsed.total_seconds() * 1000)
            allure.attach(
                str(response_time_ms),
                name="Response time (ms)",
                attachment_type=allure.attachment_type.TEXT
            )
        return response
        
    @staticmethod
    def attach_response(response, name="Response"):
        """Прикрепить полную информацию о ответе к Allure"""
        allure.attach(
            name=f"{name} - Status",
            body=str(response.status_code),
            attachment_type=allure.attachment_type.TEXT
        )
        
        allure.attach(
            name=f"{name} - Headers",
            body=json.dumps(dict(response.headers), indent=2),
            attachment_type=allure.attachment_type.JSON
        )
        
        # Если ответ маленький, прикрепляем его тело
        if len(response.content) < 10000:
            try:
                # Пробуем как JSON
                data = response.json()
                allure.attach(
                    name=f"{name} - Body (JSON)",
                    body=json.dumps(data, indent=2, ensure_ascii=False),
                    attachment_type=allure.attachment_type.JSON
                )
            except:
                # Если не JSON, прикрепляем как текст
                allure.attach(
                    name=f"{name} - Body (Text)",
                    body=response.text[:5000],
                    attachment_type=allure.attachment_type.TEXT
                )
        else:
            allure.attach(
                name=f"{name} - Body (too large, truncated)",
                body=response.text[:2000] + "...\n[Response truncated]",
                attachment_type=allure.attachment_type.TEXT
            )
        return response