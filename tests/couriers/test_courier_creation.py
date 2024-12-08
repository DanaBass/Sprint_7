import pytest

import helpers
from data.data import COURIER_DATA_WITHOUT_LOGIN, COURIER_DATA_WITHOUT_PASSWORD
from methods.courier_methods import CourierMethods


class TestCourierCreation:

    def test_create_new_courier(self):
        status_code, json, courier_data = CourierMethods.create_new_random_courier()

        assert status_code == 201 and json['ok'], f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'

    def test_not_allowed_to_create_two_same_couriers(self):
        random_courier_data = helpers.generate_new_courier_data()
        CourierMethods.create_new_courier(random_courier_data)

        status_code, json, courier_data = CourierMethods.create_new_courier(random_courier_data)

        assert status_code == 409 and json['message'] == 'Этот логин уже используется. Попробуйте другой.', f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'

    @pytest.mark.parametrize(
        "new_courier_data",
        [
            COURIER_DATA_WITHOUT_LOGIN,
            COURIER_DATA_WITHOUT_PASSWORD
        ]
    )
    def test_create_courier_without_all_requirement_parameters_returns_error(self, new_courier_data: dict):
        status_code, json, courier_data = CourierMethods.create_new_courier(new_courier_data)

        assert status_code == 400 and json['message'] == 'Недостаточно данных для создания учетной записи', f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'