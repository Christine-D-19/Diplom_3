import random
import string

import requests

from data.urls import BASE_URL
from data.user_data import UserCredentials


def _rand(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def register_user_via_api():
    payload = {
        "email": f"{_rand()}@yandex.ru",
        "password": f"{_rand(8)}A1",
        "name": f"User{_rand(5)}",
    }

    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload,
        timeout=20,
    )

    user = UserCredentials(
        email=payload["email"],
        password=payload["password"],
        name=payload["name"],
    )

    return user, response


def delete_user_via_api(access_token: str):
    return requests.delete(
        f"{BASE_URL}/api/auth/user",
        headers={"Authorization": access_token},
        timeout=20,
    )
