import factory
from faker import Faker
from django.utils import timezone

from ecommerce.models import Product, Order, OrderDetail


faker = Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    price = factory.LazyAttribute(lambda x: float(faker.random_number(digits=4)))
    stock = factory.LazyAttribute(lambda x: (faker.random_number(digits=4)))

    class Meta:
        model = Product


class OrderFactory(factory.django.DjangoModelFactory):
    date_time = timezone.now()

    class Meta:
        model = Order

class OrderDetailFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    cuantity = factory.LazyAttribute(lambda x: (faker.random_number(digits=4)))
    product = factory.SubFactory(ProductFactory)
    
    class Meta:
        model = OrderDetail
