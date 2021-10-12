from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ecommerce.views import ProductViewSet, OrderViewSet, OrderDetailViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order-detail', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
