from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Dish(models.Model):
    TYPE_CHOICES = (
        ('breakfast', 'завтрак'),
        ('dinner', 'обед'),
        ('dinner', 'ужин')
    )

    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField('ingredient', related_name='dishes')
    recipe = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, default='breakfast', max_length=16)


class DishRatingSummary(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, related_name='rating')
    value = models.IntegerField(default=0)


class DishRating(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DishHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='history')
    dish = models.ManyToManyField('Dish', related_name='history')


class DishChosen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chosen')
    dish = models.ManyToManyField('Dish', related_name='chosen')

