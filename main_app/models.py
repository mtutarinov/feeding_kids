from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField('ingredient', related_name='products')
    recipe = models.CharField(max_length=255, blank=True)
