from django.test import TestCase, Client

from rest_framework import status


class ApiTestCase(TestCase):

    client = Client()

    def test_unauthorized_get_products(self):
        response = self.client.get('/products/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthorized_get_order(self):
        response = self.client.get('/order/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthorized_get_order_detail(self):
        response = self.client.get('/order-detail/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
