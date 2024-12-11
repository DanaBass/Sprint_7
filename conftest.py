import pytest

from data.data import Courier
from methods.courier_methods import CourierMethods


@pytest.fixture
def existing_courier():
    status_code, json, courier_data = CourierMethods.create_new_random_courier()

    status_code, json = CourierMethods.login_courier(courier_data)

    yield Courier(json['id'], courier_data['login'], courier_data['password'], courier_data['firstName'])

    CourierMethods.delete_existing_courier(json['id'])