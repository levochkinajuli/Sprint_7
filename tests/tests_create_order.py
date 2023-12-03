import requests
import pytest


class TestCreateOrder:

    @pytest.mark.parametrize(
        'firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color',
        [["masha", "fokina", "Ryazan", 5, "98765678111", 3, "2023-07-06", "lll", [""]],
         ["masha", "fokina", "Ryazan", 5, "98765678111", 3, "2023-07-06", "lll", ["GREY"]],
         ["masha", "fokina", "Ryazan", 5, "98765678111", 3, "2023-07-06", "lll", ["BLACK, GREY"]]
         ]
    )
    def test_create_order_different_colors(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                    comment,
                                    color):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()
