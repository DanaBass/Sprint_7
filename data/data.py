COURIER_DATA_WITHOUT_LOGIN = {
    "password": "1234567",
    "firstName": "Test1717"
}

COURIER_DATA_WITHOUT_PASSWORD = {
    "login": "testlogin5789312578912",
    "firstName": "Test1717"
}

ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

class Courier:
    def __init__(self, courier_id, login, password, first_name):
        self.courier_id = courier_id
        self.login = login
        self.password = password
        self.first_name = first_name

    def get_login_json(self):
        return {
            "login": self.login,
            "password": self.password
        }


