from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from food.models import DishFavourite, DishHistory


@receiver(post_save, sender=User)
def post_save_create_dish_chosen(sender, instance, created, **kwargs):
    """Создает "Избранное" для пользователя."""
    if created:
        DishFavourite.objects.create(user=instance)


@receiver(post_save, sender=User)
def post_save_create_dish_history(sender, instance, created, **kwargs):
    """Создает "Историю" для пользователя."""
    if created:
        DishHistory.objects.create(user=instance)