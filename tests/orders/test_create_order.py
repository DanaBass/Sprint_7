import pytest
import allure

from data.data import ORDER_DATA
from methods.order_methods import OrderMethods

import copy

class TestOrder:

    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GRAY'],
            ['BLACK', 'GRAY'],
            []
        ]
    )
    @allure.title("Создание заказа по цвету")
    def test_create_order_by_color(self, color: list[str]):
        # На случай если в объекте ORDER_DATA будут вложенные элементы делаем глубокое копирование для избежания ошибок.
        order_data = copy.deepcopy(ORDER_DATA)
        order_data['color'] = color
        status_code, json = OrderMethods.create_order(order_data)
        assert status_code == 201 and json['track'], f'Info: status code: {status_code}, json: {json}, color: {color}'

    @allure.title("Получение списка заказов")
    def test_list_of_orders_getting(self):
        status_code, json = OrderMethods.get_all_orders(1)
        assert status_code == 200 and json['orders'], f'Info: status code: {status_code}, json: {json}'





