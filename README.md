# Проект автотестов (lesson_10)

Автотесты для веб‑приложений на Python: проверка калькулятора и сценария покупки в интернет‑магазине.  
**Стек:** `Python 3.12`, `pytest`, `Selenium`, `Allure`, `webdriver-manager`.

---

## Структура проекта

lesson_10/
├── pages/ # Page Object классы
│ ├── init.py
│ ├── calculator_page.py
│ ├── login_page.py
│ ├── inventory_page.py
│ └── checkout_page.py
├── tests/ # Тестовые сценарии
│ ├── init.py
│ ├── test_calculator.py
│ └── test_shop.py
├── venv/ # Виртуальное окружение (не коммить в git)
├── allure-results/ # Результаты прогонов тестов (XML)
├── allure-report/ # Сгенерированный HTML‑отчёт
├── conftest.py # Фикстуры pytest
└── README.md # Этот файл

## Подготовка окружения

Убедись, что установлен Python 3.12:

   ```powershell
   py -3.12 --version

Создай виртуальное окружение:

powershell
py -3.12 -m venv venv
Активируй окружение:

powershell
.\venv\Scripts\Activate.ps1
Если PowerShell блокирует скрипт, выполни один раз:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser и подтверди A.

Установи зависимости:

powershell
pip install --upgrade pip
pip install selenium webdriver-manager pytest allure-pytest
Запуск автотестов и формирование отчёта
Выполняй команды из корня проекта (lesson_10), убедившись, что виртуальное окружение активировано (в начале строки терминала видно (venv)).

Запуск тестов
powershell
pytest --import-mode=importlib --alluredir=allure-results
--import-mode=importlib нужен, чтобы pytest корректно находил локальные пакеты (pages).
Результаты тестов сохраняются в папку allure-results.
Генерация статического HTML‑отчёта
powershell
allure generate allure-results -o allure-report --clean
Отчёт будет создан в папке allure-report.
Флаг --clean очищает предыдущую версию отчёта перед генерацией новой.
Как просмотреть отчёт
powershell
allure serve allure-results
Сервер запустится и автоматически откроет отчёт в браузере. Чтобы остановить сервер, нажми Ctrl+C в терминале.

Важные примечания
Папки venv, allure-results, allure-report рекомендуется добавить в .gitignore, чтобы не коммитить временные файлы.
Браузер и драйверы. Используется webdriver-manager: драйвер для браузера (Chrome/Edge) подтягивается автоматически. Убедись, что сам браузер установлен в системе.