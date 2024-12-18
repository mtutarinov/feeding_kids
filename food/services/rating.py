from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

from food.models import DishRatingSummary, DishRating
from django.contrib.auth.models import User

class DishRatingManager:
    """Класс для работы с рейтингом блюда."""

    @staticmethod
    def add_dish_rating(total_like: DishRatingSummary):
        """Увеличивает рейтинг."""
        total_like.value += 1
        total_like.save(update_fields=['value'])

    @staticmethod
    def down_dish_rating(total_like: DishRatingSummary):
        """Уменьшает рейтинг."""
        total_like.value -= 1
        total_like.save(update_fields=['value'])

    @staticmethod
    def get_dish_rating(total_like: DishRatingSummary) -> int:
        """Возвращает рейтинг."""
        return total_like.value


def rate_dish(dish_id: int, user: User) -> int:
    """Функция для вызова DishRatingManager."""
    try:
        total_like = DishRatingSummary.objects.get(dish_id=dish_id)
    except ObjectDoesNotExist:
        total_like = DishRatingSummary.objects.create(dish_id=dish_id)
    like, created = DishRating.objects.get_or_create(user=user, dish_id=dish_id)
    if created:
        DishRatingManager.add_dish_rating(total_like)
    else:
        DishRatingManager.down_dish_rating(total_like)
        like.delete()
    return DishRatingManager.get_dish_rating(total_like)