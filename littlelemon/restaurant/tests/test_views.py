from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from ..models import Menu
from ..serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='test#123')
        self.token = Token.objects.create(user=user)

        Menu.objects.create(title='Instance1', price=15, inventory=20)
        Menu.objects.create(title='Instance2', price=25, inventory=30)
        Menu.objects.create(title='Instance3', price=35, inventory=40)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu')
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)