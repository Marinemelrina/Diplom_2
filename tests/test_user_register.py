import requests
import allure
from data import Messages, Url, UserData
from conftest import*
from helpers import create_user_data

class TestCreateCourier:
    @allure.title('Первичная регистрация пользователя с заполнением всех обязательных полей')
    def test_success_create_user(self, create_and_delete_user):
        payload = create_user_data()
        r = requests.post(Url.MAIN_URL + Url.USER_REGISTER, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Повторная регистрация пользователя ')
    def test_dublicat_create_user(self, create_and_delete_user):
        r = requests.post(Url.MAIN_URL + Url.USER_REGISTER, data=create_and_delete_user[1])
        assert r.status_code == 403 and r.json()['message'] == Messages.ERROR_403_DUBLICATE

    @allure.title('Регистрация пользователя без заполнения обязательных полей')
    @pytest.mark.parametrize('payload', (UserData.without_name, UserData.without_email, UserData.without_password))
    def test_create_user_without_some_date(self, payload):
        r = requests.post(Url.MAIN_URL + Url.USER_REGISTER, data=payload)
        assert r.status_code == 403 and r.json()['message'] == Messages.ERROR_403_WITHOUT_DATE