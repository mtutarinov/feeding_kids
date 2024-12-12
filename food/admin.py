from django.contrib import admin

from food.models import Ingredient, Dish, DishFavourite, DishHistory, DishRating, DishRatingSummary


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(DishRating)
admin.site.register(DishRatingSummary)
admin.site.register(DishFavourite)
admin.site.register(DishHistory)

