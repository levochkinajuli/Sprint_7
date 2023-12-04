import requests
import random
import string


class TestCreateCourier:

    login_pass = []

    @classmethod
    def setup_class(cls):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        cls.login_pass.append(login)
        cls.login_pass.append(password)
        cls.login_pass.append(first_name)

        return cls.login_pass

    def test_create_courier(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": self.login_pass[0], "password": self.login_pass[1], "firstName": self.login_pass[2]}
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        assert "ok" in response.json()

    def test_create_the_same_courier_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": self.login_pass[0], "password": self.login_pass[1], "firstName": self.login_pass[2]}
        response = requests.post(url, json=payload)
        assert response.status_code == 409

    def test_create_courier_without_password_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": "login", "firstName": "firstName"}
        response = requests.post(url, json=payload)
        assert response.status_code == 400

    def test_create_courier_the_same_login_error(self):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        payload = {"login": self.login_pass[0], "password": "password", "firstName": "firstName"}
        response = requests.post(url, json=payload)
        assert response.status_code == 409

    @classmethod
    def teardown_class(cls):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        payload = {"login": cls.login_pass[0], "password": cls.login_pass[1]}
        response = requests.post(url, json=payload)
        courier_id = response.json().get('id')
        url2 = f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
        payload2 = response.json()
        requests.delete(url2, json=payload2)
