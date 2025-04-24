import os
from http.client import INTERNAL_SERVER_ERROR
from types import ModuleType
from typing import Callable

from retry import retry


def configurable_retry(exceptions: tuple) -> Callable:
    if os.getenv("PROFILE") == "test":
        return lambda func: func
    return retry(exceptions, tries=5, delay=2)  # type: ignore


class DummyHttpClientException(Exception):
    pass


class DummyHttpClient:
    def __init__(self, _requests: ModuleType) -> None:
        self._requests = _requests

    @configurable_retry((DummyHttpClientException,))
    def call(self) -> None:
        response = self._requests.get("https://httpbun.com/mix/s=500")

        if response.status_code == INTERNAL_SERVER_ERROR:
            raise DummyHttpClientException("Internal server error")


class DummyHttpClientFactory:
    @staticmethod
    def make() -> DummyHttpClient:
        import requests

        return DummyHttpClient(requests)
