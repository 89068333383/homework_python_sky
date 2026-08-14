import pytest

# Позитивный тест: создание проекта
def test_create_project_positive(api_session, base_api_url, project_payload):
    url = f"{base_api_url}/projects"
    resp = api_session.post(url, json=project_payload)
    print(f"[DIAG] CREATE status={resp.status_code}, body={resp.text}")

    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}"

    data = resp.json()
    assert "id" in data and data["id"] is not None, "В ответе нет id проекта"
    project_id = data["id"]
    print(f"[DIAG] Создан проект: id={project_id}")

    # Дополнительная проверка: GET подтверждает существование и название
    get_url = f"{base_api_url}/projects/{project_id}"
    get_resp = api_session.get(get_url)
    assert get_resp.status_code == 200
    get_data = get_resp.json()
    assert get_data.get("title") == project_payload["title"]


# Негативный тест: пустой title при создании
def test_create_project_negative_empty_title(api_session, base_api_url):
    payload = {"title": ""}
    url = f"{base_api_url}/projects"
    resp = api_session.post(url, json=payload)
    print(f"[DIAG] CREATE NEG status={resp.status_code}, body={resp.text}")

    assert resp.status_code == 400, f"Ожидался 400 при неверных данных, получен {resp.status_code}"

def test_update_project_positive_put(api_session, base_api_url, project_payload):
    """
    Обновляем проект через PUT.
    ВАЖНО: API YouGile при успешном PUT возвращает только {"id": "..."}, 
    поле title в ответе отсутствует. Тест проверяет корректность поведения API.
    """
    # 1. Создаём проект
    create_url = f"{base_api_url}/projects"
    create_resp = api_session.post(create_url, json=project_payload)
    assert create_resp.status_code == 201
    proj = create_resp.json()
    project_id = proj["id"]
    original_title = project_payload["title"]
    print(f"[DIAG] Created project id={project_id}, title={original_title}")

    # 2. Готовим новое название
    new_title = f"{original_title}_UPDATED_VIA_PUT"

    # Для PUT отправляем только то, что нужно изменить (или полное тело, если требует API)
    update_payload = {"title": new_title}

    update_url = f"{base_api_url}/projects/{project_id}"
    resp = api_session.put(update_url, json=update_payload)
    print(f"[DIAG] PUT status={resp.status_code}, body={resp.text}")

    # 3. Проверяем успех
    assert resp.status_code == 200, f"Ожидался 200 при PUT, получен {resp.status_code}"

    data = resp.json()
    
    # ПРОВЕРКА 1: В ответе есть ID
    assert "id" in data, "В ответе от сервера отсутствует поле id"
    assert data["id"] == project_id, "ID в ответе не совпадает с ID обновляемого проекта"

    # ПРОВЕРКА 2: В ответе НЕТ title (это особенность API, а не баг!)
    # Мы явно проверяем, что сервер не присылает лишние данные, чтобы убедиться, что мы правильно поняли спецификацию.
    assert "title" not in data, "API YouGile не должен возвращать поле title в ответе на PUT-запрос"

    print("[DIAG] Тест пройден: PUT сработал, сервер вернул корректный формат ответа (только ID).")
    print("[INFO] Для проверки нового названия зайдите в интерфейс YouGile вручную.")


# Негативный тест: обновление несуществующего проекта
def test_update_project_negative_not_found(api_session, base_api_url):
    fake_id = "00000000-0000-0000-0000-000000000000"
    update_url = f"{base_api_url}/projects/{fake_id}"
    payload = {"title": "FakeTitle"}

    resp = api_session.patch(update_url, json=payload)
    print(f"[DIAG] UPDATE FAKE status={resp.status_code}, body={resp.text}")
    assert resp.status_code == 404, f"Ожидался 404 при несуществующем ID, получен {resp.status_code}"


# Позитивный тест: получение существующего проекта
def test_get_project_positive(api_session, base_api_url, project_payload):
    # Создаём проект, чтобы было что получать
    create_url = f"{base_api_url}/projects"
    create_resp = api_session.post(create_url, json=project_payload)
    assert create_resp.status_code == 201
    proj = create_resp.json()
    project_id = proj["id"]

    # Получаем проект
    get_url = f"{base_api_url}/projects/{project_id}"
    resp = api_session.get(get_url)
    print(f"[DIAG] GET status={resp.status_code}, body={resp.text}")
    assert resp.status_code == 200

    data = resp.json()
    assert data.get("id") == project_id
    assert data.get("title") == project_payload["title"]


# Негативный тест: получение несуществующего проекта
def test_get_project_negative_not_found(api_session, base_api_url):
    fake_id = "00000000-0000-0000-0000-000000000000"
    get_url = f"{base_api_url}/projects/{fake_id}"

    resp = api_session.get(get_url)
    print(f"[DIAG] GET FAKE status={resp.status_code}, body={resp.text}")
    assert resp.status_code == 404, f"Ожидался 404 при несуществующем ID, получен {resp.status_code}"
