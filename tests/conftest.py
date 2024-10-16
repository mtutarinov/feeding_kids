import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from tests.factories import UserFactory, ChildFactory

register(UserFactory)
register(ChildFactory)


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
