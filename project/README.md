#  MTS Shop Test Automation Framework

Автоматизированный тестовый фреймворк для тестирования интернет-магазина [shop.mts.ru](https://shop.mts.ru) с использованием **Page Object Model** и **API тестирования**.

---

## Содержание

- [Технологии](#-технологии)
- [Структура проекта](#-структура-проекта)
- [Установка и запуск](#-установка-и-запуск)
- [UI тесты](#-ui-тесты)
- [API тесты](#-api-тесты)
- [Генерация Allure отчета](#-генерация-allure-отчета)
- [Результаты тестирования](#-результаты-тестирования)

---

## Технологии

| Технология | Версия | Назначение |
|------------|--------|------------|
| **Python** | 3.14+ | Язык программирования |
| **Pytest** | 7.0+ | Фреймворк для тестирования |
| **Selenium WebDriver** | 4.0+ | Автоматизация браузера |
| **Requests** | 2.28+ | HTTP-запросы для API тестов |
| **Allure** | 2.0+ | Генерация отчетов |
| **Page Object Model** | - | Паттерн проектирования |

---

## Структура проекта

```
project/
├── config.py                  # Конфигурация и тестовые данные
├── conftest.py               # Pytest фикстуры
├── requirements.txt          # Зависимости проекта
├── test_mts_ui.py           # UI тесты (6 тестов)
├── test_api_mts.py          # API тесты (7 тестов)
├── api/
│   ├── __init__.py
│   ├── api_client.py        # Клиент для API запросов
│   └── api_assertions.py    # Проверки для API
└── pages/
    ├── __init__.py
    ├── base_page.py         # Базовый класс для страниц
    ├── main_page.py         # Главная страница
    ├── search_results_page.py  # Страница результатов поиска
    ├── product_page.py      # Страница товара
    └── basket_page.py       # Страница корзины
```

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd project
```

### Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов

```bash
# Запуск всех тестов
python -m pytest –v

# Запуск только UI тестов
pytest test_mts_ui.py -v

# Запуск только API тестов
pytest test_api_mts.py -v

# Запуск с сохранением результатов, генерации Allure отчета и его вывод
ython -m pytest -v --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report

---
## UI тесты

UI тесты используют **Page Object Model** для взаимодействия с веб-страницами.

### Список UI тестов
№	Название теста	Описание
1	test_open_main_page	Открытие главной страницы сайта          
2	test_search_and_display_products	Поиск товара "смартфон" и отображение результатов
3	test_open_product_card	Открытие карточки товара "iPhone"
4	test_add_to_cart	Добавление товара в корзину
5	test_verify_product_in_basket	Проверка наличия товара в корзине
6	test_verify_product_in_basket	Проверка ограничения количества (не более 2 шт для физ. лиц)

### Структура Page Objects

pages/
├── base_page.py          # Общие методы для всех страниц
├── main_page.py          # Главная страница (поиск, навигация)
├── search_results_page.py # Результаты поиска (выбор товара, добавление в корзину)
├── product_page.py       # Страница товара
└── basket_page.py        # Корзина (проверка товаров, изменение количества)
```

---
## API тесты

API тесты проверяют бэкенд-часть сайта через HTTP-запросы.

### Список API тестов
№	Название теста	Описание	Ожидаемый статус
1	test_site_availability	Проверка доступности главной страницы	200/301/302
2	test_get_non_existent_product	Запрос несуществующего товара	404
3	test_get_cart	Получение данных корзины	200/404
4	test_invalid_path_returns_404	Проверка метода OPTIONS для каталога	404
5	test_options_catalog	Запрос на неверный URL	200/301/302
6	test_response_headers	Проверка HTTP-заголовков ответа	200/301/302
7	test_get_categories	Получение списка категорий	200/301/302

### Структура API модулей

```
api/
├── api_client.py        # Базовый клиент с методами GET, POST, PUT, DELETE, OPTIONS
└── api_assertions.py    # Набор проверок для API ответов
```

---

## Генерация Allure отчета

### 1. Установка Allure

```bash
# Windows (через Scoop)
scoop install allure

# macOS
brew install allure

# Linux
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### 2. Запуск тестов с Allure

```bash
# Запуск тестов и сохранение результатов
pytest --alluredir=allure-results

# Генерация и открытие отчета
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### 3. Просмотр отчета в браузере

После выполнения команды `allure open allure-report` отчет автоматически откроется в браузере по адресу `http://localhost:xxxx`.

---

##  Результаты тестирования

### Итоговые результаты

Тип тестов	Количество	Результат
UI тесты	6	Все пройдены
API тесты	7	Все пройдены
Всего	13	100% PASSED


### Скриншоты в отчете
- UI тесты автоматически прикрепляют скриншоты к Allure отчету
http://127.0.0.1:58554/#behaviors/b28a1ffcb83c70ad8123073437ddc12f/e2d1394b2bf4617c/ 
- API тесты прикрепляют информацию о запросах и ответах

---

## Особенности реализации

### Page Object Model
- Каждая страница представлена отдельным классом
- Все локаторы вынесены в константы внутри классов
- Методы возвращают `self` для цепочных вызовов

### Ожидания (Waits)
- Используются только явные ожидания (`WebDriverWait`)
- `time.sleep()` не используется (запрещен в проекте)
- Все ожидания основаны на `expected_conditions`

### API Клиент
- Единый клиент для всех HTTP-методов
- Автоматическое прикрепление данных к Allure отчету
- Гибкие проверки с множеством альтернативных локаторов

### Конфигурация
- Все URL и тестовые данные в одном файле `config.py`
- Легкое переключение между средами тестирования

---

## Устранение проблем

### Проблема: ModuleNotFoundError: No module named 'requests'

**Решение:**
```bash
pip install requests
```

### Проблема: Selenium WebDriver не найден

**Решение:**
```bash
pip install webdriver-manager
```

### Проблема: Тесты не запускаются

**Решение:**
1. Проверьте, что виртуальное окружение активировано
2. Убедитесь, что все зависимости установлены: `pip install -r requirements.txt`
3. Проверьте, что файлы тестов находятся в корневой папке проекта

---

## Лицензия

Этот проект является учебным и не предназначен для коммерческого использования.
