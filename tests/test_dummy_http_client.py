from http.client import INTERNAL_SERVER_ERROR

from doublex import Stub
from expects import expect, raise_error

from src.dummy_http_client import DummyHttpClient, DummyHttpClientException


class FailedResponse:
    def __init__(self) -> None:
        self.status_code = INTERNAL_SERVER_ERROR
        self.text = "Internal server error"

    def json(self) -> dict:
        return {"detail": self.text}


class TestDummyHttpClient:
    def test_raise_exception_when_calling_the_api_returns_an_error(self) -> None:
        with Stub() as requests:
            failed_response = FailedResponse()
            requests.get("https://pmareke.com").returns(failed_response)

        http_client = DummyHttpClient(requests)

        expect(lambda: http_client.call()).to(raise_error(DummyHttpClientException))
