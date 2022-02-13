from datetime import date, timedelta

import factory
from commons.dateutils import time
import uuid
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import MenuFactory, MenuOptionsFactory


class FakeHttpResponse():
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {}


class MenuTestCase(APITestCase):

    def test_list_menu(self):
        date_menu = time(0)
        MenuFactory(date_menu=date_menu)

        url = reverse('listMenu')
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_menu_empty(self):
        url = reverse('listMenu')
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_menu_today(self):
        date_menu = time(0)
        menu = MenuFactory(date_menu=date_menu)
        MenuOptionsFactory(menu=menu)
        url = reverse('getMenu', kwargs={'uuid': menu.uuid})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['date_menu'], date_menu)

    def test_get_menu_empty_today(self):
        uuid = uuid.uuid1()
        date_menu = time(0)
        MenuFactory(date_menu=date_menu)
        url = reverse('getMenu', kwargs={'uuid': uuid})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_menu(self):
        menu_date=date.today().strftime("%Y-%m-%d")
        menu_dict = self.create_menu_data(date_menu.strftime("%Y-%m-%d"))
        response = self.client.post(reverse('createMenu', kwargs={
                    'user_id': 1}), menu_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['date_menu'], menu_dict['date_menu'])

    def create_menu_data(self, date_menu):
        data = {
            "date_menu": date_menu
            }

        return data


class MenuOptionTestCase(APITestCase):

    def test_create_option(self):
        date_menu=date.today().strftime("%Y-%m-%d")
        menu = MenuFactory(date_menu=date_menu)
        opt_dict = {'menu': menu.id,
                    'option': 3,
                    'description': 'eggs'}
        response = self.client.post(reverse('options', kwargs={
                    'user_id': 1}), opt_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['option'], opt_dict['option'])

    def test_update_menu_option(self):
        date_menu=date.today().strftime("%Y-%m-%d")
        menu = MenuFactory(date_menu=date_menu)
        menu_opt = MenuOptionsFactory(menu=menu)
        opt_dict = {'menu': menu.id,
                    'option': menu_opt.option,
                    'description': 'eggs'}
        response = self.client.put(
            reverse('options', kwargs={'user_id': 1}), opt_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'],  opt_dict['description'])
