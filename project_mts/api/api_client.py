import requests
import allure
from config import BASE_URL, TIMEOUT


class ApiClient:
    def __init__(self, base_url=BASE_URL, timeout=TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, timeout=self.timeout, **kwargs)

    def post(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, timeout=self.timeout, **kwargs)

    def put(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, timeout=self.timeout, **kwargs)

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, timeout=self.timeout, **kwargs)

    def options(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.options(url, timeout=self.timeout, **kwargs)
