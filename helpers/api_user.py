import allure
import requests
import random
import string

from data.urls import BASE_URL
from data.user_data import UserCredentials


def _rand(n=10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(n))


@allure.step("Создать пользователя через API для UI-теста")
def create_user_via_api() -> UserCredentials:
    payload = {
        "email": f"{_rand()}@yandex.ru",
        "password": f"{_rand(8)}A1", 
        "name": f"User{_rand(5)}"
    }
    resp = requests.post(f"{BASE_URL.rstrip('/')}/api/auth/register", json=payload, timeout=20)
    assert resp.status_code == 200, f"Не удалось создать пользователя через API: {resp.status_code} {resp.text}"
    return UserCredentials(email=payload["email"], password=payload["password"], name=payload["name"])
