import requests


class TestCreateCourier:
    courier = {}

    @classmethod
    def setup_class(cls):
        cls.courier["login"] = "vasiaivanov234"
        cls.courier["password"] = "12345"
        cls.courier["firstName"] = "vasia"

    def test_create_courier(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = self.courier
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        assert "ok" in response.json()

    def test_create_the_same_courier_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = self.courier
        response = requests.post(url, json=payload)
        assert response.status_code == 409

    def test_create_courier_without_password_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": self.courier["login"], "firstName": self.courier["firstName"]}
        response = requests.post(url, json=payload)
        assert response.status_code == 400

    def test_create_courier_the_same_login_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": self.courier["login"], "password": "54321", "firstName": "natasha"}
        response = requests.post(url, json=payload)
        assert response.status_code == 409

    @classmethod
    def teardown_class(cls):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": cls.courier["login"], "password": cls.courier["password"]}
        response = requests.post(url, json=payload)
        courier_id = response.json().get('id')
        url2 = f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
        payload2 = response.json()
        requests.delete(url2, json=payload2)
