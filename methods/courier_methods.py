import requests

import helpers
from data.urls import BASE_URL, COURIERS_URL


class CourierMethods:

    @staticmethod
    def create_new_random_courier():
        courier_data = helpers.generate_new_courier_data()

        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=courier_data)

        return response.status_code, response.json(), courier_data

    @staticmethod
    def create_new_courier(courier_data: dict):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=courier_data)

        return response.status_code, response.json(), courier_data

    @staticmethod
    def login_courier(courier_login_data: dict):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=courier_login_data)
        return response.status_code, response.json()


    @staticmethod
    def delete_existing_courier(courier_id: int):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{courier_id}')

        return response.status_code, response.json()