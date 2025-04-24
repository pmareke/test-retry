```sh
make slow-test

PYTHONPATH=. uv run pytest -x -ra tests/
========================= test session starts =========================
tests/test_dummy_http_client.py .                                [100%]
========================= 1 passed in 10.96s ==========================
```

```sh
make fast-test

PYTHONPATH=. PROFILE=test uv run pytest -x -ra tests/
========================= test session starts =========================
tests/test_dummy_http_client.py .                                [100%]
========================= 1 passed in 0.62s ===========================
```
