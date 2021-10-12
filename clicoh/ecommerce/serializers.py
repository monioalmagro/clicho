from rest_framework import serializers

from .models import Product, Order, Order_Detail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_total(self, obj: Order) -> int:
        return obj.get_total()

    def get_total_usd(self, obj: Order) -> int:
        return obj.get_total_usd()

class Order_DetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order_Detail
        fields = '__all__'


class OrderDetailSerializer(OrderSerializer):
    order = Order_DetailSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'