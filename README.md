```sh
make slow-test

uv run pytest -x -ra tests/
========================= test session starts =========================
tests/test_dummy_http_client.py .                                [100%]
========================= 1 passed in 4.04s ===========================
```

```sh
make fast-test

PROFILE=test uv run pytest -x -ra tests/
========================= test session starts =========================
tests/test_dummy_http_client.py .                                [100%]
========================= 1 passed in 0.03s ===========================
```
