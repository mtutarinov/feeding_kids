import factory
from faker import Faker

from main_app.models import Ingredient, Dish
from food import ingredients, dishes, dish_descriptions

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = factory.Iterator(ingredients)


class DishFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dish

    name = factory.Iterator(dishes)
    recipe = factory.Iterator(dish_descriptions)

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.ingredients.add(*extracted)
