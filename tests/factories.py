import factory
from django.contrib.auth.models import User

from children.models import Child
from faker_food import dish_descriptions, dishes, ingredients
from food.models import (
    Allergen,
    Dish,
    DishFavourite,
    DishHistory,
    DishRating,
    Ingredient,
)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")


class ChildFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child

    uuid = factory.Faker("uuid4")
    name = factory.Faker("first_name")
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


class DishHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DishHistory

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def dish(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.dish.add(*extracted)


class DishFavouriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DishFavourite

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def dish(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.dish.add(*extracted)


class AllergenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Allergen

    uuid = factory.Faker("uuid4")
    ingredient = factory.SubFactory(IngredientFactory)
    child = factory.SubFactory(ChildFactory)
