import requests
import allure
from config import BASE_URL, TIMEOUT


class ApiClient:
    """Базовый клиент для API запросов"""
    
    def __init__(self, base_url=BASE_URL, timeout=TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        
    def get(self, endpoint, **kwargs):
        """GET запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, timeout=self.timeout, **kwargs)
        
    def post(self, endpoint, **kwargs):
        """POST запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, timeout=self.timeout, **kwargs)
        
    def put(self, endpoint, **kwargs):
        """PUT запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, timeout=self.timeout, **kwargs)
        
    def delete(self, endpoint, **kwargs):
        """DELETE запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, timeout=self.timeout, **kwargs)
        
    def options(self, endpoint, **kwargs):
        """OPTIONS запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.options(url, timeout=self.timeout, **kwargs)
        
    def head(self, endpoint, **kwargs):
        """HEAD запрос"""
        url = f"{self.base_url}{endpoint}"
        return self.session.head(url, timeout=self.timeout, **kwargs)
        
    def attach_response(self, response, name="Response"):
        """Прикрепить информацию о ответе к Allure"""
        allure.attach(
            name=f"{name} - Status",
            body=str(response.status_code),
            attachment_type=allure.attachment_type.TEXT
        )
        
        allure.attach(
            name=f"{name} - Headers",
            body=str(dict(response.headers)),
            attachment_type=allure.attachment_type.TEXT
        )
        
        # Если ответ маленький, прикрепляем его тело
        if len(response.content) < 10000:
            try:
                allure.attach(
                    name=f"{name} - Body",
                    body=response.text[:5000],  # Обрезаем длинные ответы
                    attachment_type=allure.attachment_type.TEXT
                )
            except:
                pass