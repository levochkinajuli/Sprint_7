import requests


class TestLoginCourier:
    courier = {}

    @classmethod
    def setup_class(cls):
        cls.courier["login"] = "vasiaivanov234"
        cls.courier["password"] = "12345"
        cls.courier["firstName"] = "vasia"
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = cls.courier
        requests.post(url, json=payload)

    def test_login_courier(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": self.courier["login"], "password": self.courier["password"]}
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    def test_incorrect_login_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": "login", "password": self.courier["password"]}
        response = requests.post(url, json=payload)
        assert response.status_code == 404

    def test_login_without_password_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": self.courier["login"], "password": ""}
        response = requests.post(url, json=payload)
        assert response.status_code == 400

    def test_login_not_exist_user_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": "jkikl", "password": "4444"}
        response = requests.post(url, json=payload)
        assert response.status_code == 404

    @classmethod
    def teardown_class(cls):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": cls.courier["login"], "password": cls.courier["password"]}
        response = requests.post(url, json=payload)
        courier_id = response.json().get('id')
        url2 = f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
        payload2 = response.json()
        requests.delete(url2, json=payload2)
