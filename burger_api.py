import requests
from data import Url
import allure
class BurgerAPI:
    @allure.step("Метод для создания пользователя с заполнением полей")
    def create_user(body):
        return requests.post(Url.MAIN_URL + Url.USER_REGISTER, json=body)
    @allure.step("Метод для авторизации пользователя")
    def login_user(body):
        return requests.post(Url.MAIN_URL + Url.USER_LOGIN, json=body)
    @allure.step("Метод для удаления пользователя")
    def delete_user(body):
        response = BurgerAPI.login_user(body)
        if 'accessToken' in response:
            requests.delete(Url.MAIN_URL + Url.USER_DATA)
    @allure.step("Метод для получения списка ингредиентов")
    def ingredients_get_method():
        return requests.get(Url.MAIN_URL + Url.INGRIDIENTS_URL)

    @allure.step('Создать заказ')
    def order_create(ingredients: list, token):
        payload={"ingredients": ingredients}
        header={"Authorization": token}
        return requests.post(Url.MAIN_URL + Url.ORDER, data=payload, headers=header)

    @allure.step("Метод для получения списка заказов")
    def list_of_orders(token):
        header={"Authorization": token}
        return requests.get(Url.MAIN_URL + Url.ORDER, headers=header)

    @allure.step("Метод для внесения изменений в данные пользователя")
    def remove_user_data(body, token):
        header={"Authorization": token}
        return requests.patch(Url.MAIN_URL + Url.USER_DATA, json=body, headers=header)