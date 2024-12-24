from django.db.models import Count, Q

from food.models import Dish


class DishConstructor:
    """Работает с ингредиентами из корзины."""

    @staticmethod
    def get(available_ids, allergen_ids):
        dishes = (
            Dish.objects.annotate(
                allergen_ingredients=Count(
                    "ingredients", filter=Q(ingredients__in=allergen_ids)
                ),
                matched_ingredients=Count(
                    "ingredients", filter=Q(ingredients__in=available_ids)
                ),
                total_ingredients=Count("ingredients"),
            )
            .filter(matched_ingredients__gte=1)
            .order_by(
                "allergen_ingredients", "-matched_ingredients", "total_ingredients"
            )
        )
        return dishes
