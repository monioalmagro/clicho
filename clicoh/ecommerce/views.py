from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .exeptions import StockInProductError, CuantityZeroError, ProductRepetitionOrderError
from .models import Product, Order, Order_Detail
from .serializers import ProductSerializer, OrderSerializer, Order_DetailSerializer, OrderDetailSerializer
from .utils import Util


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    util = Util()

    def create(self, request, *args, **kwargs):
        try:
            self.util.check_stock(request)
            self.util.create_order(request)
            return Response({},status=201)
        except ProductRepetitionOrderError as e:
            return Response({'error':str(e)},status=404)
        except StockInProductError as e:
            return Response({'error':str(e)},status=404)
        except CuantityZeroError as e:
            return Response({'error':str(e)},status=404)
        except:
            return Response({"error":"Check Format request."},status=404)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        try:
            self.util.check_stock(request)
            self.util.update_partial_order(request, pk)
            return Response({},status=200)
        except ProductRepetitionOrderError as e:
            return Response({'error':str(e)},status=404)
        except StockInProductError as e:
            return Response({'error':str(e)},status=404)
        except CuantityZeroError as e:
            return Response({'error':str(e)},status=404)
        except:
            return Response({"error":"Check Format request."},status=404)

    def destroy(self, request, pk=None):
        try:
            self.util.destroy_order(request, pk)
            return Response({},status=200)
        except:
            return Response({"error":"Check Format Request."},status=404)


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = Order_DetailSerializer
    queryset = Order_Detail.objects.all()
