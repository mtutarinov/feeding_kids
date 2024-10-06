from rest_framework.serializers import ModelSerializer
from .models import Dish, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('product', 'name')