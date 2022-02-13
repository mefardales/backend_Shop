from datetime import date, timedelta

import pytz
from commons.dateutils import time

import factory
from menu.factories import MenuFactory, MenuOptionsFactory
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from user.factories import UserFactory
import random

from .factories import OrderFactory


class FakeHttpResponse():
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {}


class UserMenuTestCase(APITestCase):

        def test_get_ordes_today(self):
        menu_date = time(0)
        menu = MenuFactory(menu_date=menu_date)
        menu_opt = MenuOptionsFactory(menu=menu)
        user = UserFactory()
        order = OrderFactory(menu_option=menu_opt, user=user, order_date=menu_date)
        url = reverse('getOrder', kwargs={'user_id': order.user_id})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['menu_option'], order.menu_option_id)

    def test_get_ordes_empty_today(self):
        menu_date=date.today()
        menu = MenuFactory(menu_date=menu_date)
        menu_opt = MenuOptionsFactory(menu=menu)
        user = UserFactory()
        url = reverse('getOrder', kwargs={'user_id': user.id})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def create_order_data(self, menu_id, menu_option):
        data = {
            "menu": menu_id,
            "menu_option": menu_option,
            "quantity": random.randint(1, 4),
            "specification": "chiles en nopales"
}

        return data
