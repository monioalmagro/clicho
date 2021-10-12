from .models import Product, Order_Detail, Order
from .exeptions import StockInProductError, CuantityZeroError, ProductRepetitionOrderError


class Util:

    def create_order(self, request, order=None):
        if order is None:
            order = Order.objects.create()
        for x in request.data.get('order'):
            cuantity = x.get('cuantity')
            product_id = x.get('product')
            product = Product.objects.get(pk=product_id)
            Order_Detail.objects.create(
                cuantity=cuantity,
                product = product,
                order = order
            )

    def manage_stock(self, new, old, product_id):
        stock = Product.objects.get(pk=product_id).stock
        new_stock = stock + (old-new)
        Product.objects.filter(pk=product_id).update(stock=new_stock)

    def back_to_stock(self, list):
        for x in list:
            x.product.stock = x.product.stock + x.cuantity
            x.product.save()

    def update_partial_order(self, request, pk):
        products_in_order = Order_Detail.objects.filter(order_id=pk)
        if products_in_order:
            self.back_to_stock(products_in_order)
        products_in_order = Order_Detail.objects.filter(order_id=pk).delete()
        order = Order.objects.get(pk=pk)
        self.create_order(request, order=order)

    def destroy_order(self, request, pk):
        products_in_order = Order_Detail.objects.filter(order_id=pk)
        if products_in_order:
            self.back_to_stock(products_in_order)
        products_in_order = Order_Detail.objects.filter(order_id=pk).delete()
        order = Order.objects.filter(pk=pk).delete()

    def check_stock(self, request):
        list_of_control = []
        list_of_lines = request.data.get('order')
        for x in list_of_lines:
            if x.get('cuantity') == 0:
                raise CuantityZeroError('Error when Cuantity in order-detail is zero')
            if ((x.get('product')) in list_of_control):
                raise ProductRepetitionOrderError('Product repetition in the same order.')
            list_of_control.append(x.get('product'))
            stock_of_product = Product.objects.get(pk=x.get('product')).stock
            if stock_of_product < x.get('cuantity'):
                raise StockInProductError('Error when trying to select a product without stock.')
