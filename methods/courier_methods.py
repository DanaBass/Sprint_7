import requests
import allure
import helpers

from data.urls import BASE_URL, COURIERS_URL


class CourierMethods:

    @staticmethod
    @allure.title("Создание нового случайного курьера")
    @allure.step("Создание нового случайного курьера")
    @allure.description("Этот метод создает нового курьера с случайными данными.")
    def create_new_random_courier():
        courier_data = helpers.generate_new_courier_data()

        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=courier_data)

        return response.status_code, response.json(), courier_data

    @staticmethod
    @allure.title("Создание нового курьера с заданными данными")
    @allure.step("Создание нового курьера")
    @allure.description("Этот метод создает нового курьера с заданными данными.")
    def create_new_courier(courier_data: dict):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=courier_data)

        return response.status_code, response.json(), courier_data

    @staticmethod
    @allure.title("Авторизация курьера")
    @allure.step("Авторизация курьера")
    @allure.description("Этот метод авторизует курьера по предоставленным данным.")
    def login_courier(courier_login_data: dict):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=courier_login_data)
        return response.status_code, response.json()


    @staticmethod
    @allure.title("Удаление существующего курьера")
    @allure.step("Удаление существующего курьера")
    @allure.description("Этот метод удаляет курьера по ID.")
    def delete_existing_courier(courier_id: int):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{courier_id}')

        return response.status_code, response.json()