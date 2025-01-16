from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from food.models import (
    Allergen,
    Dish,
    DishFavourite,
    DishHistory,
    DishRating,
    Ingredient,
)


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("name",)


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "ingredients", "recipe", "description", "type")


class ShowDishSerializer(ModelSerializer):
    allergen_ingredients = serializers.SerializerMethodField()
    matched_ingredients = serializers.SerializerMethodField()
    total_ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = (
            "name",
            "allergen_ingredients",
            "matched_ingredients",
            "total_ingredients",
        )

    @staticmethod
    def get_allergen_ingredients(obj):
        return obj.allergen_ingredients

    @staticmethod
    def get_matched_ingredients(obj):
        return obj.matched_ingredients

    @staticmethod
    def get_total_ingredients(obj):
        return obj.total_ingredients


class DishRatingSerializer(ModelSerializer):
    class Meta:
        model = DishRating
        fields = ("dish", "value")


class DishHistorySerializer(ModelSerializer):
    class Meta:
        model = DishHistory
        fields = ("user", "dish")


class DishFavouriteSerializer(ModelSerializer):
    class Meta:
        model = DishFavourite
        fields = ("user", "dish")


class AllergenSerializer(ModelSerializer):
    class Meta:
        model = Allergen
        fields = ("uuid", "ingredient", "child")
