import allure
import requests
from data import IngredientsData, Url, Messages
from conftest import create_and_delete_user


class TestOrder:
    @allure.title(
        "Проверка создания заказа под авторизованным пользователем"
    )
    def test_order_with_login(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.post(Url.MAIN_URL + Url.ORDER, headers=token,
                          data=IngredientsData.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title(
        "Проверка создания заказа под авторизованным пользователем и несуществующим хэшем ингредиентов"
    )
    def test_order_with_login(self, create_and_delete_user):
        r = requests.post(Url.MAIN_URL + Url.ORDER, data=IngredientsData.incorrect_ingredients)
        assert r.status_code == 500 and 'Internal Server Error' in r.text

    @allure.title(
        "Проверка создания заказа под авторизованным пользователем и без ингредиентов"
    )
    def test_order_with_login_and_without_ingredients(self, create_and_delete_user):
        r = requests.post(Url.MAIN_URL + Url.ORDER)
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"


    @allure.title("Проверка создания заказа без авторизации")
    def test_order_without_login(self, create_and_delete_user):
        r = requests.post(Url.MAIN_URL + Url.ORDER, data=IngredientsData.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Проверка получения заказа авторизованным пользователем")
    def test_get_order_with_authorised_user_success(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        requests_create_order = requests.post(Url.MAIN_URL + Url.ORDER, headers=token,
                                              data=IngredientsData.correct_ingredients)
        response_get_order = requests.get(Url.MAIN_URL + Url.ORDER, headers=token)
        assert (response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] ==
                requests_create_order.json()['order']['number'])

    @allure.title("Проверка получения заказа неавторизованным пользователем")
    def test_get_order_user_without_authorisation_fail(self, create_and_delete_user):
        r = requests.get(Url.MAIN_URL + Url.ORDER)
        assert r.status_code == 401 and r.json()['message'] == Messages.ERROR_401_AUTHORIZED_FOR_ORDER_LIST

