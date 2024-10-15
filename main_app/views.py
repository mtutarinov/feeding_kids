from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main_app.models import Dish, Ingredient
from main_app.serializers import IngredientSerializer, DishSerializer


class ProductViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
