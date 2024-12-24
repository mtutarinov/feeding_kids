import uuid

from django.contrib.auth.models import User
from django.db import models

from children.models import Child


class Ingredient(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, unique=True)


class Allergen(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    ingredient = models.ForeignKey(
        Ingredient, related_name="ingredients", on_delete=models.CASCADE
    )
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="allergens")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ingredient", "child"], name="uniq_ingredient_child"
            ),
        ]


class Dish(models.Model):
    TYPE_CHOICES = ((1, "завтрак"), (2, "обед"), (3, "ужин"))
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField("ingredient", related_name="dishes")
    recipe = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=1, db_index=True)


class DishRatingSummary(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, related_name="rating")
    value = models.IntegerField(default=0)


class DishRating(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "dish"], name="uniq_user_dish"),
        ]


class DishHistory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    dish = models.ForeignKey(
        "Dish", related_name="history", on_delete=models.CASCADE, blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "dish"], name="uniq_history"),
        ]


class DishFavourite(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourite")
    dish = models.ForeignKey(
        "Dish", related_name="favourite", on_delete=models.CASCADE, blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "dish"], name="uniq_favourite"),
        ]
