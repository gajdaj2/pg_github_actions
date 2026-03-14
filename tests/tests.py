import os

import requests


BASE_URL = os.getenv("TEST_BASE_URL", "http://127.0.0.1:8000")


def test_root_returns_hello_world() -> None:
    response = requests.get(f"{BASE_URL}/", timeout=5)

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_calc_adds_two_numbers() -> None:
    response = requests.get(
        f"{BASE_URL}/calc",
        params={"a": 2, "b": 3},
        timeout=5,
    )

    assert response.status_code == 200
    assert response.json() == 5


def test_calc_requires_b_parameter() -> None:
    response = requests.get(f"{BASE_URL}/calc", params={"a": 2}, timeout=5)

    assert response.status_code == 422

