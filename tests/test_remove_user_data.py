from helpers import RegisterUserWithoutDate
from conftest import*


class TestRemoveUserData:
    @allure.title("Проверка изменения email авторизованного пользователя")
    def test_remove_email_with_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        registered_user_payload["email"] = RegisterUserWithoutDate.new_email
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title("Проверка изменения пароля авторизованного пользователя")
    def test_remove_password_with_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        registered_user_payload["password"] = RegisterUserWithoutDate.new_password
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title("Проверка изменения email и пароля авторизованного пользователя")
    def test_remove_email_and_password_with_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        registered_user_payload["email"] = RegisterUserWithoutDate.generate_email()
        registered_user_payload["password"] = RegisterUserWithoutDate.new_password
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title("Проверка изменения email неавторизованного пользователя")
    def test_remove_email_without_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = "no_token"
        registered_user_payload["email"] = RegisterUserWithoutDate.generate_email()
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 401 and response.json()["success"] == False

    @allure.title("Проверка изменения пароля неавторизованного пользователя")
    def test_remove_password_without_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = "no_token"
        registered_user_payload["password"] = RegisterUserWithoutDate.new_password
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 401 and response.json()["success"] == False

    @allure.title("Проверка изменения email и пароля неавторизованного пользователя")
    def test_remove_email_and_password_without_login(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = "no_token"
        registered_user_payload["email"] = RegisterUserWithoutDate.generate_email()
        registered_user_payload["password"] = RegisterUserWithoutDate.new_password
        payload = {
            "email": registered_user_payload["email"],
            "password": registered_user_payload["password"],
        }

        response = BurgerAPI.remove_user_data(payload, token)

        assert response.status_code == 401 and response.json()["success"] == False
