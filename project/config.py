BASE_URL = "https://shop.mts.ru"
API_BASE_URL = "https://shop.mts.ru"  
TIMEOUT = 10

class TestData:
 # UI тесты
    SEARCH_TERM = "смартфон"
    IPHONE_TERM = "смартфон Apple iPhone 12 Pro"
    TARGET_KEYWORD = "iPhone"
    MAX_QUANTITY = "5"
    EXPECTED_MODAL_TEXT = "юридическое лицо"
    
    # API тесты
    NON_EXISTENT_PRODUCT_ID = "999999999"
    INVALID_PATH = "/this-path-does-not-exist"
    
    # Селекторы для UI
    SEARCH_INPUT = "input[name='q']"
    FIND_BUTTON = "//span[contains(@class, 'button__text') and normalize-space()='Найти']"
    PRODUCT_CARD = "a[href*='/product/']"
    BUY_BUTTON = "button.mtsds-button"
    MODAL_TITLE = "div.mtsds-modal-page__header p.mtsds-modal-page__header-title"
    BASKET_BUTTON = "a[href='/personal/basket'] .mtsds-button__text-container"
    QUANTITY_INPUT = "input[name='input-quantity']"
    MODAL_LIMIT_TEXT = "//div[contains(@class, 'dialog-modal__confirm-text') and contains(text(), 'юридическое лицо')]"