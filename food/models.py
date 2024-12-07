from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField('ingredient', related_name='products')
    recipe = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)


class DishRatingSummary(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, related_name='rating')
    value = models.IntegerField(default=0)


class DishRating(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DishHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='history')
    history = models.ManyToManyField('Dish', related_name='history')


class DishChosen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chosen')
    chosen = models.ManyToManyField('Dish', related_name='chosen')

