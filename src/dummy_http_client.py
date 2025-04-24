from http.client import INTERNAL_SERVER_ERROR
from types import ModuleType

from src.retry_unless_test import retry_unless_test


class DummyHttpClientException(Exception):
    pass


class DummyHttpClient:
    def __init__(self, _requests: ModuleType) -> None:
        self._requests = _requests

    @retry_unless_test((DummyHttpClientException,))
    def call(self) -> None:
        response = self._requests.get("https://httpbun.com/mix/s=500")

        if response.status_code == INTERNAL_SERVER_ERROR:
            raise DummyHttpClientException("Internal server error")


class DummyHttpClientFactory:
    @staticmethod
    def make() -> DummyHttpClient:
        import requests

        return DummyHttpClient(requests)
