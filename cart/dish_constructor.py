from django.db.models import Count, Q

from food.models import Dish


class DishConstructor:
    """Работает с ингредиентами из корзины."""

    @staticmethod
    def get(available_ids):
        dishes = (
            Dish.objects.annotate(
                total_ingredients=Count("ingredients"),
                matched_ingredients=Count(
                    "ingredients", filter=Q(ingredients__in=available_ids)
                ),
            )
            .filter(matched_ingredients__gte=1)
            .order_by("-matched_ingredients", "total_ingredients")
        )
        return dishes
