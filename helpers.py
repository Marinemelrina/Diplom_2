import requests
import random
import string
import allure
from random import choice
from data import Url
from burger_api import BurgerAPI

@allure.step('Формирование тела запроса для создания пользователя')
def get_user_registration_body():
    @allure.step("Генерируем рандомную строку")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("Генерируем рандомный email")
    def generate_email():
        letters = string.ascii_letters
        email_name = ''.join(random.choice(letters) for i in range(10))

        domains = ['ya.ru', 'gmail.com', 'mail.ru', 'rambler.com']
        email_domain = random.choice(domains)

        email = email_name + '@' + email_domain

        return email

    email = generate_email()
    name = generate_random_string(10)
    password = generate_random_string(10)


    payload = {
        "email": email,
        "name": name,
        "password": password
    }
    return payload

@allure.step('Формирование тела запроса для создания пользователя и возвращения адреса почты и пароля')
def register_new_user_and_return_email_password(get_new_data):
    payload = get_new_data
    user_create_url = f'{Url.MAIN_URL}{Url.USER_REGISTER}'
    response = requests.post(url=user_create_url, data=payload)
    if response.status_code == 200:
        return payload

class RegisterUserWithoutDate:
    @allure.step("Генерируем рандомную строку")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    name = generate_random_string(10)
    password = generate_random_string(10)
    new_name = name[::-1]
    new_password = password[::-1]

    @allure.step("Генерируем рандомный email")
    def generate_email():
        letters = string.ascii_letters
        email_name = ''.join(random.choice(letters) for i in range(10))

        domains = ['ya.ru', 'gmail.com', 'mail.ru', 'rambler.com']
        email_domain = random.choice(domains)

        email = email_name + '@' + email_domain

        return email
    email = generate_email()
    new_email = generate_random_string(3)+email

@allure.step("Генерируем рандомный список ингредиентов")
def get_random_ingredients():
    response = BurgerAPI.ingredients_get_method()
    ingredients = []

    for ingredient in response.json()['data']:
        ingredients.append(ingredient['_id'])

    random_ingredients_list = []
    for ingredient in range(3):
        random_ingredients_list.append(choice(ingredients))

    return random_ingredients_list