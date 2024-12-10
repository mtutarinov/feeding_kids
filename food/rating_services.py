from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

from food.models import DishRatingSummary, DishRating
from django.contrib.auth.models import User

class DishRatingManager:
    """Класс для работы с рейтингом блюда."""

    @staticmethod
    def add_dish_rating(total_like: DishRatingSummary):
        """Увеличивает рейтинг."""
        total_like.value = F('value') + 1
        total_like.save()

    @staticmethod
    def down_dish_rating(total_like: DishRatingSummary):
        """Уменьшает рейтинг."""
        total_like.value = F('value') - 1
        total_like.save()

    @staticmethod
    def get_dish_rating(total_like: DishRatingSummary) -> int:
        """Возвращает рейтинг."""
        total_like.refresh_from_db()
        return total_like.value


def rating_services(id: id, user: User) -> int:
    """Функция для вызова DishRatingManager."""
    try:
        total_like = DishRatingSummary.objects.get(dish_id=id)
    except ObjectDoesNotExist:
        total_like = DishRatingSummary.objects.create(dish_id=id)
    like, created = DishRating.objects.get_or_create(user=user, dish_id=id)
    if created:
        DishRatingManager.add_dish_rating(total_like)
    else:
        DishRatingManager.down_dish_rating(total_like)
        like.delete()
    return DishRatingManager.get_dish_rating(total_like)