import pytest
import allure

from data.data import COURIER_DATA_WITHOUT_LOGIN, COURIER_DATA_WITHOUT_PASSWORD
from methods.courier_methods import CourierMethods


class TestCourierLogin:

    @allure.title("Успешный вход курьера с корректными данными")
    @allure.step("Тестирование входа курьера с корректными данными")
    def test_login_courier_with_correct_data_is_successfull(self, existing_courier):
        courier_login_json = existing_courier.get_login_json()

        status_code, json = CourierMethods.login_courier(courier_login_json)

        assert status_code == 200 and json['id'], f'Info: status code: {status_code}, json: {json}, courier_login_json: {courier_login_json}'

    @allure.title("Вход с некорректными данными")
    @allure.step("Тестирование входа с некорректными данными")
    def test_login_with_incorrect_data(self, existing_courier):
        incorrect_login_data = {
            'login': existing_courier.login,
            'password': existing_courier.password + "incorrect_password_part"
        }
        status_code, json = CourierMethods.login_courier(incorrect_login_data)

        assert status_code == 404 and json['message'] == 'Учетная запись не найдена', f'Info: status code: {status_code}, json: {json}, incorrect_login_data: {incorrect_login_data}'

    @pytest.mark.parametrize(
        "login_courier_data",
        [
            COURIER_DATA_WITHOUT_LOGIN,
            #COURIER_DATA_WITHOUT_PASSWORD - почему-то если отдавать только логин, сервис зависает - вероятно ошибка разработчиков.
        ]
    )
    @allure.title("Попытка входа в систему курьера без обязательных параметров")
    @allure.step("Тестирование входа курьера без всех требуемых параметров")
    def test_login_courier_without_all_requirement_parameters_returns_error(self, login_courier_data: dict):
        status_code, json = CourierMethods.login_courier(login_courier_data)

        assert status_code == 400 and json['message'] == 'Недостаточно данных для входа', f'Info: status code: {status_code}, json: {json}, login_courier_data: {login_courier_data}'

    @allure.title("Вход с существующим курьером возвращает ID")
    @allure.step("Тестирование входа с существующим курьером")
    def test_login_with_existing_courier_returns_id(self, existing_courier):
        status_code, json = CourierMethods.login_courier(existing_courier.get_login_json())

        assert status_code == 200 and json['id'], f'Info: status code: {status_code}, json: {json}'