from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from food.models import DishHistory, DishFavourite

class Manager:
    model = None
    distinct_fields = []

    @classmethod
    def get(cls, user: User):
        qs = cls.model.objects.filter(user=user)
        if cls.distinct_fields:
            return qs.distinct(*cls.distinct_fields)

    @classmethod
    def add(cls, user: User, dish_id: int):
        try:
            cls.model.objects.create(user=user, dish_id=dish_id)
        except IntegrityError:
            pass

    @classmethod
    def delete(cls, user: User, dish_id: int):
        cls.model.objects.filter(user=user, dish_id=dish_id).delete()


class HistoryManager(Manager):
    model = DishHistory
    distinct_fields = ['user', 'dish']


class FavouriteManager(Manager):
    model = DishFavourite
    distinct_fields = ['user', 'dish']
