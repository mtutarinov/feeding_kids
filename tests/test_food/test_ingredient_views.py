import pytest
from rest_framework import status

from food.models import Ingredient
from tests.conftest import ingredient, anon_client, client
from tests.factories import IngredientFactory

INGREDIENT_LIST_URL = '/api/v1/ingredients/'

@pytest.mark.django_db
def test_ingredients_list_client(client):
    IngredientFactory.create_batch(2)
    response = client.get(INGREDIENT_LIST_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert 'name' in response.data[0]


@pytest.mark.django_db
def test_ingredients_list_anon_client(anon_client):
    IngredientFactory.create_batch(2)
    response = anon_client.get(INGREDIENT_LIST_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_detail_anon_client(anon_client, ingredient):
    response = anon_client.get(INGREDIENT_LIST_URL + f'{ingredient.pk}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_detail_client(client, ingredient):
    response = client.get(INGREDIENT_LIST_URL + f'{ingredient.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data['name'] == ingredient.name


@pytest.mark.django_db
def test_ingredients_post_anon_client(anon_client):
    data = {
        'name': 'test_food'
    }
    response = anon_client.post(INGREDIENT_LIST_URL, data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_post_client(client):
    data = {
        'name': 'test_food'
    }
    response = client.post(INGREDIENT_LIST_URL, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    ingredient = Ingredient.objects.get(id=response.data.serializer.instance.id)
    assert len(response.data) == 1
    assert response.data['name'] == ingredient.name


@pytest.mark.django_db
def test_ingredients_put_anon_client(anon_client, ingredient):
    data = {
        'name': 'test_food'
    }
    response = anon_client.put(INGREDIENT_LIST_URL + f'{ingredient.id}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_put_client(client, ingredient):
    data = {
        'name': 'test_food'
    }
    response = client.put(INGREDIENT_LIST_URL + f'{ingredient.id}/', data=data)
    assert response.status_code == status.HTTP_200_OK
    ingredient.refresh_from_db()
    assert len(response.data) == 1
    assert response.data['name'] == 'test_food'


@pytest.mark.django_db
def test_ingredients_patch_anon_client(anon_client, ingredient):
    data = {
        'name': 'test_food'
    }
    response = anon_client.patch(INGREDIENT_LIST_URL + f'{ingredient.id}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_patch_client(client, ingredient):
    data = {
        'name': 'test_food'
    }
    response = client.patch(INGREDIENT_LIST_URL + f'{ingredient.id}/', data=data)
    assert response.status_code == status.HTTP_200_OK
    ingredient.refresh_from_db()
    assert len(response.data) == 1
    assert response.data['name'] == 'test_food'


@pytest.mark.django_db
def test_ingredients_delete_anon_client(anon_client, ingredient):
    response = anon_client.delete(INGREDIENT_LIST_URL + f'{ingredient.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_ingredients_delete_client(client, ingredient):
    response = client.delete(INGREDIENT_LIST_URL + f'{ingredient.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT