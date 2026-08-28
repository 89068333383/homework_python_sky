import allure


class ApiAssertions:
    @staticmethod
    def assert_status_code(response, expected_status):
        with allure.step(f"Проверяем статус-код: ожидается {expected_status}"):
            assert (
                response.status_code == expected_status
            ), f"Ожидался статус {expected_status}, получен {response.status_code}"
        return response

    @staticmethod
    def assert_status_in_range(response, status_codes):
        with allure.step(f"Проверяем статус-код: ожидается один из {status_codes}"):
            assert (
                response.status_code in status_codes
            ), f"Ожидался один из статусов {status_codes}, получен {response.status_code}"
        return response

    @staticmethod
    def assert_response_not_empty(response):
        with allure.step("Проверяем, что ответ не пустой"):
            assert len(response.content) > 0, "Ответ сервера пустой"
        return response

    @staticmethod
    def assert_content_type(response, expected_type="text/html"):
        with allure.step(f"Проверяем Content-Type: ожидается {expected_type}"):
            content_type = response.headers.get("Content-Type", "")
            assert content_type != "", "Заголовок Content-Type отсутствует"
            assert (
                expected_type in content_type.lower()
            ), f"Неверный Content-Type. Ожидался {expected_type}, получен: {content_type}"
        return response

    @staticmethod
    def assert_text_contains(response, text):
        """Проверить, что текст ответа содержит указанную строку"""
        with allure.step(f"Проверяем наличие текста '{text}' в ответе"):
            assert (
                text in response.text or text.lower() in response.text.lower()
            ), f"Текст '{text}' не найден в ответе"
        return response

    @staticmethod
    def attach_response_time(response):
        with allure.step("Фиксируем время ответа"):
            response_time_ms = int(response.elapsed.total_seconds() * 1000)
            allure.attach(
                str(response_time_ms),
                name="Response time (ms)",
                attachment_type=allure.attachment_type.TEXT,
            )
        return response

    @staticmethod
    def attach_response(response, name="Response"):
        """Прикрепить информацию о ответе к Allure отчету"""
        allure.attach(
            name=f"{name} - Status",
            body=str(response.status_code),
            attachment_type=allure.attachment_type.TEXT,
        )

        allure.attach(
            name=f"{name} - Headers",
            body=str(dict(response.headers)),
            attachment_type=allure.attachment_type.TEXT,
        )

        # Если ответ небольшой, прикрепляем тело
        if len(response.content) < 10000:
            try:
                allure.attach(
                    name=f"{name} - Body",
                    body=response.text[:5000],
                    attachment_type=allure.attachment_type.TEXT,
                )
            except:
                pass
        else:
            allure.attach(
                name=f"{name} - Body (truncated)",
                body=response.text[:2000] + "...\n[Response truncated]",
                attachment_type=allure.attachment_type.TEXT,
            )
        return response
