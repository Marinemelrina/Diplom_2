from helpers import RegisterUserWithoutDate
from burger_api import BurgerAPI
from data import Messages
import allure
import pytest

class TestLoginUser:
    @allure.title("Проверка авторизации ранее зарегистрированного пользователя")
    @pytest.mark.parametrize('email, password, name', [(RegisterUserWithoutDate.email, RegisterUserWithoutDate.password, RegisterUserWithoutDate.name)])
    def test_success_login_user(self, email, password, name):

        payload={
            "email": email,
            "password": password,
            "name": name

        }
        create_user = BurgerAPI.create_user(payload)
        payload_login={
            "email": email,
            "password": password
        }
        login_user=BurgerAPI.login_user(payload_login)
        BurgerAPI.delete_user(payload)

        assert login_user.status_code == 200 and 'accessToken' in login_user.json() and 'refreshToken' in login_user.json() and \
               login_user.json()['success'] == True

    @allure.title("Проверка авторизации пользователя с рандомными данными")
    def test_fake_login_user(self):
        payload_login = {
            "email": RegisterUserWithoutDate.generate_email(),
            "password": RegisterUserWithoutDate.password
        }
        login_user = BurgerAPI.login_user(payload_login)

        assert login_user.status_code == 401 and login_user.json()['message'] == Messages.ERROR_401_AUTHORIZED