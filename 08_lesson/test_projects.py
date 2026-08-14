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


# ---------------------------------------------------------
# НОВЫЙ ТЕСТ: попытка изменить название проекта → ожидаем ошибку
# ---------------------------------------------------------
def test_update_project_cannot_change_title(api_session, base_api_url, project_payload):
    """
    YouGile не позволяет менять название проекта через API.
    Этот тест проверяет, что система корректно отклоняет такую попытку.
    """
    # 1. Создаём проект
    create_url = f"{base_api_url}/projects"
    create_resp = api_session.post(create_url, json=project_payload)
    assert create_resp.status_code == 201
    proj = create_resp.json()
    project_id = proj["id"]
    original_title = project_payload["title"]
    
    print(f"[DIAG] Created project id={project_id}, title={original_title}")

    # 2. Пытаемся обновить название (чего делать нельзя)
    update_url = f"{base_api_url}/projects/{project_id}"
    new_title = f"{original_title}_UPDATED"
    update_payload = {"title": new_title}

    resp = api_session.patch(update_url, json=update_payload)
    print(f"[DIAG] PATCH status={resp.status_code}, body={resp.text}")

    # 3. Ожидаем, что сервер НЕ вернёт 200, потому что менять title нельзя.
    # В зависимости от версии API это может быть 400/403/404/405 — главное, не 200.
    assert resp.status_code != 200, (
        f"Неожиданно получили {resp.status_code} при попытке сменить название проекта. "
        f"YouGile запрещает менять title через API."
    )
    
    # Дополнительно: можно ожидать конкретно 400 или 403, если знаешь, что отдаёт API
    # assert resp.status_code in (400, 403), f"Ожидалась ошибка доступа/валидации, а получено {resp.status_code}"
    
    print("[DIAG] Тест пройден: корректно отклонена попытка смены названия проекта.")


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
