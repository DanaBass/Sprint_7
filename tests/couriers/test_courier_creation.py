import pytest
import helpers
import allure

from data.data import COURIER_DATA_WITHOUT_LOGIN, COURIER_DATA_WITHOUT_PASSWORD
from data.messages import COURIER_LOGIN_TAKEN, NOT_ENOUGH_DATA_FOR_CREATE
from methods.courier_methods import CourierMethods


class TestCourierCreation:

    @allure.title("Создание нового курьера")
    def test_create_new_courier(self):
        status_code, json, courier_data = CourierMethods.create_new_random_courier()

        assert status_code == 201 and json['ok'], f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'

    @allure.title("Попытка создать двух одинаковых курьеров")
    def test_not_allowed_to_create_two_same_couriers(self):
        random_courier_data = helpers.generate_new_courier_data()
        CourierMethods.create_new_courier(random_courier_data)

        status_code, json, courier_data = CourierMethods.create_new_courier(random_courier_data)

        assert status_code == 409 and json['message'] == COURIER_LOGIN_TAKEN, f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'

    @pytest.mark.parametrize(
        "new_courier_data",
        [
            COURIER_DATA_WITHOUT_LOGIN,
            COURIER_DATA_WITHOUT_PASSWORD
        ]
    )
    @allure.title("Создание курьера с неполными данными")
    def test_create_courier_without_all_requirement_parameters_returns_error(self, new_courier_data: dict):
        status_code, json, courier_data = CourierMethods.create_new_courier(new_courier_data)

        assert status_code == 400 and json['message'] == NOT_ENOUGH_DATA_FOR_CREATE, f'Info: status code: {status_code}, json: {json}, courier_data: {courier_data}'