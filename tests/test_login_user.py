import allure
import requests
from conftest import create_and_delete_user
from data import Url, Messages
from helpers import create_user_login

class TestLoginUser:
    @allure.title("Проверка успешной авторизации пользователя")
    def test_user_login_success(self, create_and_delete_user):
        r = requests.post(Url.MAIN_URL + Url.USER_LOGIN, data=create_and_delete_user[2])
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Проверка при авторизации с неверным логином и паролем")
    def test_user_login_incorrect_login_data_fail(self, create_and_delete_user):
        payload = create_user_login()
        r = requests.post(Url.MAIN_URL + Url.USER_LOGIN, data=payload)
        assert r.status_code == 401 and r.json()['message'] == Messages.ERROR_401_AUTHORIZED