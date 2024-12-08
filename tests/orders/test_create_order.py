import pytest

from methods.order_methods import OrderMethods


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
    def test_create_order_by_color(self, color: list, order_data: dict):
        order_data['color'] = color
        status_code, json = OrderMethods.create_order(order_data)
        assert status_code == 201 and json['track'], f'Info: status code: {status_code}, json: {json}, color: {color}'

    def test_list_of_orders_getting(self):
        status_code, json = OrderMethods.get_all_orders(1)
        assert status_code == 200 and json['orders'], f'Info: status code: {status_code}, json: {json}'





