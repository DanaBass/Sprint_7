COURIER_DATA_WITHOUT_LOGIN = {
    "password": "1234567",
    "firstName": "Test1717"
}

COURIER_DATA_WITHOUT_PASSWORD = {
    "login": "testlogin5789312578912",
    "firstName": "Test1717"
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


