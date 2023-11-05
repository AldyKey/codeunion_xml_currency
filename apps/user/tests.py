from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import User


class UserRegisterViewTest(APITestCase):
    def test_user_registration(self):
        url = reverse('register_user')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'password_repeat': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login(self):
        url = reverse('login_view')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_user_login(self):
        url = reverse('login_view')
        data = {
            'username': 'invalidusername',
            'password': 'invalidpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

