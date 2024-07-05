
class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    USER_REGISTER = '/api/auth/register'
    USER_LOGIN = '/api/auth/login'
    USER_DATA = '/api/auth/user'
    ORDER = '/api/orders'
    GET_ALL_ORDERS = '/api/orders/all'
    INGRIDIENTS_URL = '/api/ingredients'

class Messages:
    ERROR_403_DUBLICATE = 'User already exists'
    ERROR_403_WITHOUT_DATE = 'Email, password and name are required fields'
    ERROR_401_AUTHORIZED = 'email or password are incorrect'
    ERROR_401_AUTHORIZED_FOR_ORDER_LIST = 'You should be authorised'

class UserData:
    without_name = {"email": "test@yandex.ru", "password": "test"}
    without_email = {"password": "test", "name": "test"}
    without_password = {"email": "test@yandex.ru", "name": "test"}


class IngredientsData:
    correct_ingredients = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
    incorrect_ingredients = {
        "ingredients": [
            "bdaaa6d",
            "bdaaa73"
        ]
    }
