import factory
from faker import Faker
from django.contrib.auth.models import User

from food.models import Ingredient, Dish, DishRating
from faker_food import ingredients, dishes, dish_descriptions
from children.models import Child

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

class ChildFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child

    uuid = factory.Faker('uuid4')
    name = factory.Faker('first_name')
    age = 1
    months = 2
    mother = factory.SubFactory(UserFactory)

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

class DishRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DishRating

    dish = factory.SubFactory(DishFactory)
    value = 0