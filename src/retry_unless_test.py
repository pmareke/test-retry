import os
from typing import Callable

from retry import retry


def retry_unless_test(exceptions: tuple[type[Exception]]) -> Callable:
    if os.getenv("PROFILE") == "test":
        return lambda func: func
    return retry(exceptions, tries=3, delay=1, backoff=3)  # type: ignore
