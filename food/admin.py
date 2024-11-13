from django.contrib import admin
from food.models import Ingredient, Dish

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Dish)