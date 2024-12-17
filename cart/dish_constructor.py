from food.models import Dish


class DishConstructor:
    """Работает с ингредиентами из корзины."""

    @staticmethod
    def get(ingredients_ids):
        return Dish.objects.filter(ingredients__in=ingredients_ids).distinct()
