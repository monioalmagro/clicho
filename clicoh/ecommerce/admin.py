from django.contrib import admin
from .models import Product, Order_Detail, Order


admin.site.register(Product)
admin.site.register(Order_Detail)
admin.site.register(Order)
