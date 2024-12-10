from rest_framework.serializers import ModelSerializer
from food.models import Dish, Ingredient, DishRating, DishHistory, DishChosen


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'ingredients', 'recipe', 'description', 'type')


class ShowDishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name',)


class DishRatingSerializer(ModelSerializer):
    class Meta:
        model = DishRating
        fields = ('dish', 'value')


class DishHistorySerializer(ModelSerializer):
    class Meta:
        model = DishHistory
        fields = ('user', 'dish')


class DishChosenSerializer(ModelSerializer):
    class Meta:
        model = DishChosen
        fields = ('user', 'dish')