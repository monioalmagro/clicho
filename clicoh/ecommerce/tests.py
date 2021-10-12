#from django.test import TestCase

#from decimal import Decimal
#import pytest
#from pytest_factoryboy import register

#from rest_framework import status
#from django.urls import reverse

#from exchange_rate.tests.factories import ExchangeRateFactory
#from .factories import ProductFactory, OrderFactory, OrderDetailFactory

#register(ProductFactory)
#register

""" @pytest.mark.django_db
class TestExchangeRateViewSet:

    # current
    def test_current_unauthorized_get(self, client):
        response = client.get(reverse('exchange-rate-current'))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_current_without_exchange_rate_returns_404(self, user_client):
        response = user_client.get(reverse('exchange-rate-current'))
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_current_exchange_rate(self, user_client, exchange_rate):
        response = user_client.get(reverse('exchange-rate-current'))
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['date'] == str(exchange_rate.date)
        assert Decimal(data['amount']) == exchange_rate.ceg_amount()
 """
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status
class ApiTestCase(TestCase):

    client = Client()
    client2 = Client()

    product:dict = {"name": "mouse", "price": 500.0, "stock": 5}
    product_2:dict = {"name": "Mouse", "price": 555.0, "stock": 3}

    def register_a_product(self):
        response = self.client.post('/products/', self.product)
        return response
        
    def test_register_a_product(self):
        response = self.register_a_product()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get('name') == self.product['name']

    def test_edit_a_product(self):
        response = self.register_a_product()
        response_1 = self.client.get('/products/')
        pk = response_1.data[0].get('id')
        response_2 = self.client2.put('/products/'+str(pk), self.product_2)
        import pdb;pdb.set_trace()
        assert response.status_code == status.HTTP_201_CREATED

    def test_status_code(self):
        
        response = self.client.get('/products/')
        assert response.status_code == status.HTTP_200_OK

    