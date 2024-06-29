
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


