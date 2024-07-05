import pytest
from helpers import *
from data import Url
import requests

@pytest.fixture(scope="function")
def create_and_delete_user():
    payload = create_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Url.MAIN_URL+Url.USER_REGISTER, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(Url.MAIN_URL + Url.USER_DATA, headers={'Authorization': f'{token}'})