import allure
from conftest import *
from helpers import generate_random_string
from data import Messages
class TestRemoveUserData:
    @allure.title("Проверка изменения email авторизованного пользователя")
    def test_remove_email_with_login(self, create_and_delete_user):
        new_email = f'{generate_random_string(5)}@yandex.ru'
        payload = {'email': new_email}
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.patch(Url.MAIN_URL + Url.USER_DATA, headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == new_email

    @allure.title("Проверка изменения пароля авторизованного пользователя")
    def test_remove_password_with_login(self, create_and_delete_user):
        new_password = generate_random_string(5)
        payload = {'password': new_password}
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.patch(Url.MAIN_URL + Url.USER_DATA, headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Успешное изменение имени авторизованного пользователя')
    def test_change_user_name_authorised_user_success(self, create_and_delete_user):
        new_name = generate_random_string(5)
        payload = {'name': new_name}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Url.MAIN_URL + Url.USER_DATA, headers=token, data=payload)
        assert response.status_code == 200 and response.json()['user']['name'] == new_name

    @allure.title('Проверка при измении данных неавторизованного пользователя')
    @pytest.mark.parametrize('payload', [{'email': f'{generate_random_string(5)}@yandex.ru'},
                                         {'password': generate_random_string(5)},
                                         {'name': generate_random_string(5)}])
    def test_change_user_data_without_authorization_fail(self, payload):
        r = requests.patch(Url.MAIN_URL + Url.USER_DATA, data=payload)
        assert r.status_code == 401 and r.json()['message'] == Messages.ERROR_401_AUTHORIZED_FOR_ORDER_LIST
