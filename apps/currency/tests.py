from rest_framework.test import APITestCase
from django.urls import reverse
from django.conf import settings
from datetime import datetime, timedelta
import jwt

from .models import Currency
from apps.user.models import User


class CurrencyViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        token_payload = {
            'exp': int((datetime.now() + timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            'iat': datetime.now().timestamp(),
            'username': self.user.username
        }
        self.jwt_token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
        self.currency = Currency.objects.create(name="USDT", rate=1.0)

    def test_currency_list_view_not_authorized(self):
        url = reverse('currency_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)

    def test_currency_list_view_authorized(self):
        url = reverse('currency_list')
        headers = {'HTTP_AUTHORIZATION': f'Bearer {self.jwt_token}'}
        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, 200)

    def test_currency_retrieve_view_not_authorized(self):
        url = reverse('currency_get', kwargs={'pk': self.currency.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)

    def test_currency_retrieve_view_authorized(self):
        url = reverse('currency_get', kwargs={'pk': self.currency.id})
        headers = {'HTTP_AUTHORIZATION': f'Bearer {self.jwt_token}'}
        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, 200)