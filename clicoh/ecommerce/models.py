from django.db import models

import requests


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    def add_stock(self, number):
        self.stock = self.stock + number
        return self.stock


class Order(models.Model):
    date_time = models.DateField(auto_now_add=True)

    def get_total(self):
        return sum([int(ol.cuantity)*ol.product.price for ol in self.order.all()])

    def get_total_usd(self):
        url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
        resp = requests.get(url)
        lista = resp.json()
        for x in lista:
            if x['casa'].get('nombre') == "Dolar Blue":
                venta = x['casa'].get('venta')
        venta = venta.replace(",",".")
        pesos = sum([int(ol.cuantity)*ol.product.price for ol in self.order.all()])
        valor_en_dolares = int(pesos) * float(venta)
        return valor_en_dolares


    def __str__(self) -> str:
        return str(self.date_time)


class Order_Detail(models.Model):
    cuantity = models.IntegerField()
    product = models.ForeignKey(
        'ecommerce.Product', on_delete=models.CASCADE,
        related_name='product',
    )
    order = models.ForeignKey(
        'ecommerce.Order', on_delete=models.CASCADE,
        related_name='order',
    )

    def __str__(self) -> str:
        return str(self.cuantity) +"-"+ self.product.name

    def save(self, *args, **kwargs):
        product = Product.objects.get(pk=self.product.id)
        new_stock = product.stock - self.cuantity
        product.stock = new_stock
        product.save()
        super().save(*args, **kwargs)

    def update(self, *args, **kargs):
        algo=""
        pass

