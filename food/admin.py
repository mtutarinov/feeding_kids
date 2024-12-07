from django.contrib import admin

from food.models import Ingredient, Dish, DishChosen, DishHistory, DishRating


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(DishRating)
admin.site.register(DishChosen)
admin.site.register(DishHistory)

