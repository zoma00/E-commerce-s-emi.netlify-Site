from django.shortcuts import render
from rest_framework import routers
from django.urls import path, include
#from rest_framework import viewsets
from products.models import Product, Category, Order, OrderItem
from .view_sets import CategorysViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()
router.register('Product',CategorysViewSet )
router.register('Category',ProductViewSet )
router.register('Order',OrderViewSet )
router.register('OrderItem', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]