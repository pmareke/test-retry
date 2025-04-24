from expects import expect, raise_error

from src.dummy_http_client import DummyHttpClientException, DummyHttpClientFactory


class TestDummyHttpClient:
    def test_raise_exception_when_calling_the_api_returns_an_error(self) -> None:
        http_client = DummyHttpClientFactory.make()

        expect(lambda: http_client.call()).to(
            raise_error(DummyHttpClientException, "Internal server error")
        )
