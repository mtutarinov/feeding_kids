import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import (
    AllergenFactory,
    ChildFactory,
    DishFactory,
    DishFavouriteFactory,
    DishHistoryFactory,
    IngredientFactory,
    UserFactory,
)

register(UserFactory)
register(ChildFactory)
register(IngredientFactory)
register(DishFactory)
register(DishHistoryFactory)
register(DishFavouriteFactory)
register(AllergenFactory)


@pytest.fixture
def user() -> User:
    return UserFactory.create()


def _create_token_for_user(user):
    token = RefreshToken.for_user(user)
    return token.access_token


@pytest.fixture
def anon_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture
def client(user: User) -> APIClient:
    client = APIClient()
    client.user = user
    token = _create_token_for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    return client


@pytest.fixture
def child(user: User):
    return ChildFactory.create(mother=user)


@pytest.fixture
def ingredient():
    return IngredientFactory.create()


@pytest.fixture
def dish():
    return DishFactory.create()


@pytest.fixture
def allergen(child, ingredient):
    return AllergenFactory.create(child=child, ingredient=ingredient)
