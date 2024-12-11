import requests
import allure

from data.urls import BASE_URL, ORDERS_URL


class OrderMethods:

    @staticmethod
    @allure.step("Создание нового заказа")
    def create_order(order_data):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=order_data)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Получение всех заказов")
    def get_all_orders(limit=None):
        url = f'{BASE_URL}{ORDERS_URL}'
        if limit is not None:
            url += f'?limit={limit}'

        response = requests.get(url)
        return response.status_code, response.json()

