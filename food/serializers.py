from rest_framework.serializers import ModelSerializer
from food.models import Dish, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'ingredients', 'recipe')

class ShowDishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', )