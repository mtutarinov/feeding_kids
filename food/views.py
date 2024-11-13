from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from food.models import Dish, Ingredient
from food.serializers import IngredientSerializer, DishSerializer


class ProductViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated, )


class DishViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
