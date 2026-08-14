import os
import uuid
import pytest
import requests

@pytest.fixture(scope="session")
def base_api_url():
    return "https://ru.yougile.com/api-v2"

@pytest.fixture(scope="session")
def auth_token(base_api_url):
    """
    1. Получает токен через POST /auth/keys (как в твоём примере).
    2. Сразу проверяет его через GET /users/me.
    3. Возвращает токен для использования в тестах.
    """
    login = os.getenv("YOUGILE_LOGIN")
    password = os.getenv("YOUGILE_PASSWORD")
    company_id = os.getenv("YOUGILE_COMPANY_ID")

    if not all([login, password, company_id]):
        pytest.fail(
            "Нужны переменные окружения: YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID"
        )

    # Шаг 1: Получаем токен
    url_auth = f"{base_api_url}/auth/keys"
    payload = {
        "login": login,
        "password": password,
        "companyId": company_id,
    }

    resp = requests.post(url_auth, json=payload)
    print(f"[DIAG] Auth request status={resp.status_code}, body={resp.text}")

    assert resp.status_code == 201, f"Ожидался 201 при получении токена, получен {resp.status_code}"

    data = resp.json()
    assert "key" in data and data["key"], "В ответе нет поля key"
    token = data["key"]
    print("[DIAG] Токен успешно получен")

    # Шаг 2: Проверяем токен (ИСПРАВЛЕНО: не убираем /api-v2)
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    
    # Правильный URL: base_api_url + /users/me
    me_resp = session.get(f"{base_api_url}/users/me")
    print(f"[DIAG] Проверка токена: status={me_resp.status_code}, body={me_resp.text}")
    
    assert me_resp.status_code == 200, f"Токен не работает: {me_resp.status_code}"
    
    me = me_resp.json()
    print(f"[DIAG] Пользователь: {me.get('name')}, Компания: {me.get('company_name')}")

    return token

@pytest.fixture
def api_session(auth_token):
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {auth_token}"})
    yield session
    session.close()

@pytest.fixture
def project_payload():
    unique_suffix = uuid.uuid4().hex[:8]
    return {"title": f"TestProject_{unique_suffix}"}