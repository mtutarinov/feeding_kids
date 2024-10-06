from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main_app.models import Product, Dish
from main_app.serializers import ProductSerializer, DishSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
