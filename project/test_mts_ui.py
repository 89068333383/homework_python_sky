import pytest
import allure
from config import TestData
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


### ТК1 ОТКРЫТИЕ САЙТА
@allure.feature("Открытие сайта")
@allure.story("Открыть главную страницу сайта")
@allure.title("Тест: Открытие страницы сайта")
def test_open_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.attach_screenshot("Главная страница сайта")


### ТК2 ПОИСК И ОТОБРАЖЕНИЕ ТОВАРА
@allure.feature("Поиск")
@allure.story("Поиск товара 'смартфон' с закрытием попапа Flocktory")
@allure.title("Тест: Поиск товара и его отображение на странице")
def test_search_and_display_products(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.search_and_navigate(TestData.SEARCH_TERM)
    
    search_results = SearchResultsPage(driver)
    search_results.wait_for_products()
    print("Список товаров загружен.")
    search_results.attach_search_results_screenshot()


### ТК3 ПРОСМОТР КАРТОЧКИ ТОВАРА
@allure.feature("Каталог товаров")
@allure.story("Переход из каталога в карточку товара")
@allure.title("Тест: открытие карточки товара кликом по ней")
def test_open_product_card(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.search_and_navigate(TestData.IPHONE_TERM)
    
    search_results = SearchResultsPage(driver)
    product_link = search_results.find_product_by_keyword(TestData.TARGET_KEYWORD)
    search_results.click_product_and_verify(product_link)
    
    product_page = ProductPage(driver)
    product_page.verify_product_page_loaded()
    print("Открыта карточка товара")


### ТК4 ДОБАВЛЕНИЕ ТОВАРА В КОРЗИНУ
@allure.feature("Каталог товаров")
@allure.story("Добавление товара в корзину")
@allure.title("Тест: добавление товара в корзину кнопкой «Купить»")
def test_add_to_cart(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.search_and_navigate(TestData.IPHONE_TERM)
    
    search_results = SearchResultsPage(driver)
    product_link = search_results.find_product_by_keyword(TestData.TARGET_KEYWORD)
    search_results.add_product_to_cart(product_link)
    print("Клик по кнопке выполнен!")
    search_results.attach_screenshot("Скриншот: Товар добавлен в корзину (модалка видна)")


### ТК5 ПРОВЕРКА НАЛИЧИЯ ТОВАРА В КОРЗИНЕ
@allure.feature("Каталог товаров")
@allure.story("Добавление товара в корзину")
@allure.title("Тест: проверка наличия товара в корзине")
def test_verify_product_in_basket(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.search_and_navigate(TestData.IPHONE_TERM)
    
    search_results = SearchResultsPage(driver)
    product_link = search_results.find_product_by_keyword(TestData.TARGET_KEYWORD)
    search_results.add_product_to_cart(product_link)
    print("✅ Клик по кнопке выполнен!")
    
    search_results.go_to_basket_from_modal()
    print(f"✅ Перешли в корзину: {driver.current_url}")
    
    basket_page = BasketPage(driver)
    basket_page.verify_basket_content(TestData.TARGET_KEYWORD)
    print("✅ Слово 'iPhone' найдено в тексте страницы корзины!")
    basket_page.attach_basket_screenshot()


### ТК6 ПРОВЕРКА ОГРАНИЧЕНИЯ КОЛИЧЕСТВА ТОВАРА
@allure.feature("Каталог товаров")
@allure.story("Добавление товара в корзину")
@allure.title("Тест: проверка невозможности добавления более 2-х товаров для физического лица")
def test_quantity_limit_for_individual(driver):
    # Шаг 1: Открытие и поиск
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.search_and_navigate(TestData.IPHONE_TERM)
    
    # Шаг 2: Поиск товара
    search_results = SearchResultsPage(driver)
    product_link = search_results.find_product_by_keyword(TestData.TARGET_KEYWORD)
    
    # Шаг 3: Добавление в корзину
    search_results.add_product_to_cart(product_link)
    print("✅ Клик по кнопке выполнен!")
    
    # Шаг 4: Переход в корзину из модалки
    search_results.go_to_basket_from_modal()
    print(f"✅ Перешли в корзину: {driver.current_url}")
    
    # Шаг 5: Проверка ограничения количества
    basket_page = BasketPage(driver)
    basket_page.set_quantity_and_trigger_limit(TestData.MAX_QUANTITY)
    print("✅ Модальное окно с ограничением найдено — тест достиг цели!")