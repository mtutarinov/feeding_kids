from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from food.models import DishHistory, DishFavourite

class Manager:
    """Шаблон менеджера для работы с Историей и Избранным."""
    model = None
    distinct_fields = []

    @classmethod
    def get(cls, user: User):
        """Показывает список."""
        qs = cls.model.objects.filter(user=user)
        if cls.distinct_fields:
            return qs.distinct(*cls.distinct_fields)

    @classmethod
    def add(cls, user: User, dish_id: int):
        """Добавляет в список."""
        try:
            cls.model.objects.create(user=user, dish_id=dish_id)
        except IntegrityError:
            pass

    @classmethod
    def delete(cls, user: User, dish_id: int):
        """Удаляет из списка."""
        cls.model.objects.filter(user=user, dish_id=dish_id).delete()


class HistoryManager(Manager):
    model = DishHistory
    distinct_fields = ['user', 'dish']


class FavouriteManager(Manager):
    model = DishFavourite
    distinct_fields = ['user', 'dish']
