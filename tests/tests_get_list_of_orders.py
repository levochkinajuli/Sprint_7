import requests


class TestGetListOfOrders:
    courier = {}

    @classmethod
    def setup_class(cls):
        cls.courier["login"] = "vasiaivanov234"
        cls.courier["password"] = "12345"
        cls.courier["firstName"] = "vasia"
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = cls.courier
        requests.post(url, json=payload)

    def test_get_list_of_orders(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": self.courier["login"], "password": self.courier["password"]}
        response = requests.post(url, json=payload)
        courier_id = response.json().get('id')
        url2 = f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId={courier_id}'
        payload = {"courierId": courier_id}
        response = requests.get(url2, json=payload)
        assert response.status_code == 200
        assert 'orders' in response.json()

    @classmethod
    def teardown_class(cls):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": cls.courier["login"], "password": cls.courier["password"]}
        response = requests.post(url, json=payload)
        courier_id = response.json().get('id')
        url2 = f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
        payload2 = response.json()
        requests.delete(url2, json=payload2)
