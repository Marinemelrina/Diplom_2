from helpers import RegisterUserWithoutDate
from data import Messages
from conftest import*


class TestOrder:
    @allure.title(
        "Проверка создания заказа под авторизованным пользователем с ингредиентами"
    )
    def test_order_with_login_and_ingredients(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        ingredient = helpers.get_random_ingredients()
        created_order = BurgerAPI.order_create(ingredient, token)

        assert (
            created_order.status_code == 200 and created_order.json()["success"] == True
        )

    @allure.title(
        "Проверка создания заказа под авторизованным пользователем и несуществующим хэшем ингредиентов"
    )
    def test_order_with_login_and_incorrect_ingredients(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        ingredient = {"ingredients": RegisterUserWithoutDate.name}
        created_order = BurgerAPI.order_create(ingredient, token)

        assert created_order.status_code == 500

    @allure.title(
        "Проверка создания заказа под авторизованным пользователем и без ингредиентов"
    )
    def test_order_with_login_without_ingredients(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        ingredient = []
        created_order = BurgerAPI.order_create(ingredient, token)

        assert (
            created_order.status_code == 400
            and created_order.json()["success"] == False
        )

    @allure.title("Проверка создания заказа без авторизации с ингредиентами")
    def test_order_without_login_with_ingredients(self):
        token = "no_token"
        ingredient = helpers.get_random_ingredients()
        created_order = BurgerAPI.order_create(ingredient, token)

        assert (
            created_order.status_code == 200 and created_order.json()["success"] == True
        )

    @allure.title(
        "Проверка создания заказа без авторизации с несуществующим хэшем ингредиентов"
    )
    def test_order_without_login_and_incorrect_ingredients(self):
        token = "no_token"
        ingredient = {"ingredients": RegisterUserWithoutDate.name}
        created_order = BurgerAPI.order_create(ingredient, token)

        assert created_order.status_code == 500

    @allure.title("Проверка создания заказа без авторизации и без ингредиентов")
    def test_order_without_login_and_without_ingredients(self):
        token = "no_token"
        ingredient = []
        created_order = BurgerAPI.order_create(ingredient, token)

        assert (
            created_order.status_code == 400
            and created_order.json()["success"] == False
        )

    @allure.title("Проверка получения списка заказов авторизованного пользователя")
    def test_get_order_list_for_login_user(self, registered_user_payload):
        response = BurgerAPI.create_user(registered_user_payload)
        token = response.json()["accessToken"]
        ingredient = helpers.get_random_ingredients()
        created_order = BurgerAPI.order_create(ingredient, token)

        order_list = BurgerAPI.list_of_orders(token)

        assert order_list.status_code == 200 and order_list.json()["success"] == True

    @allure.title("Проверка получения списка заказов неавторизованного пользователя")
    def test_get_order_list_without_login_user(self):
        token = "no_token"
        ingredient = helpers.get_random_ingredients()
        created_order = BurgerAPI.order_create(ingredient, token)

        order_list = BurgerAPI.list_of_orders(token)

        assert (
            order_list.status_code == 401
            and order_list.json()["success"] == False
            and order_list.json()["message"]
            == Messages.ERROR_401_AUTHORIZED_FOR_ORDER_LIST
        )
