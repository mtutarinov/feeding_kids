import pytest
from rest_framework import status

from food.models import Dish
from tests.conftest import anon_client, client, ingredient
from tests.factories import IngredientFactory, DishFactory

DISH_LIST_URL = '/api/v1/dishes/'

@pytest.mark.django_db
def test_dishes_list_anon_client(anon_client):
    response = anon_client.get(DISH_LIST_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_list_client(client):
    ingredients = IngredientFactory.create_batch(4)
    dishes = DishFactory.create_batch(2, ingredients=ingredients)
    response = client.get(DISH_LIST_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == dishes[0].name
    assert len(response.data[0]['ingredients']) == 4 == len(ingredients) == len(response.data[1]['ingredients'])
    assert response.data[0]['ingredients'] == [ingredient.id for ingredient in ingredients] == response.data[1][
        'ingredients']
    assert response.data[0]['recipe'] == dishes[0].recipe
    assert response.data[1]['name'] == dishes[1].name
    assert response.data[1]['recipe'] == dishes[1].recipe


@pytest.mark.django_db
def test_dishes_detail_anon_client(anon_client, dish):
    response = anon_client.get(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_detail_client(client):
    ingredients = IngredientFactory.create_batch(2)
    dish = DishFactory.create(ingredients=ingredients)
    response = client.get(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5
    assert response.data['name'] == dish.name
    assert len(response.data['ingredients']) == len(ingredients) == 2
    assert response.data['ingredients'] == [ingredient.id for ingredient in ingredients]
    assert response.data['recipe'] == dish.recipe
    assert response.data['description'] == dish.description
    assert response.data['type'] == dish.type


@pytest.mark.django_db
def test_dishes_post_client(client):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test',
        'description': 'test',
        'type': 'breakfast'
    }
    response = client.post(DISH_LIST_URL, data=data)
    dish = Dish.objects.get(id=response.data.serializer.instance.id)
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 5
    assert response.data['name'] == dish.name == 'test'
    assert len(response.data['ingredients']) == len(ingredients) == dish.ingredients.count() == 2
    assert response.data['ingredients'] == ingredients == [ingredient.id for ingredient in dish.ingredients.all()]
    assert response.data['recipe'] == dish.recipe == 'test'
    assert response.data['description'] == dish.description == 'test'
    assert response.data['type'] == dish.type == 'breakfast'


@pytest.mark.django_db
def test_dishes_post_anon_client(anon_client):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test',
        'description': 'test',
        'type': 'breakfast'
    }
    response = anon_client.post(DISH_LIST_URL, data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_put_anon_client(anon_client, dish):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test',
        'description': 'test',
        'type': 'breakfast'
    }
    response = anon_client.put(DISH_LIST_URL + f'{dish.id}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_put_client(client, dish):
    ingredients = [ingr.id for ingr in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test',
        'description': 'test',
        'type': 'breakfast'
    }
    response = client.put(DISH_LIST_URL + f'{dish.id}/', data=data)
    assert response.status_code == status.HTTP_200_OK
    dish.refresh_from_db()
    assert len(response.data) == 5
    assert response.data['name'] == dish.name == 'test'
    assert len(response.data['ingredients']) == len(ingredients) == dish.ingredients.count() == 2
    assert response.data['ingredients'] == ingredients == [ingr.id for ingr in dish.ingredients.all()]
    assert response.data['recipe'] == dish.recipe == 'test'
    assert response.data['description'] == dish.description == 'test'
    assert response.data['type'] == dish.type == 'breakfast'


@pytest.mark.django_db
def test_dishes_patch_anon_client(anon_client, dish):
    data = {
        'name': 'test'
    }
    response = anon_client.patch(DISH_LIST_URL + f'{dish.id}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_patch_client(client, dish):
    data = {
        'name': 'test'
    }
    response = client.patch(DISH_LIST_URL + f'{dish.id}/', data=data)
    dish.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5
    assert response.data['name'] == dish.name == 'test'


@pytest.mark.django_db
def test_dishes_delete_anon_client(anon_client, dish):
    response = anon_client.delete(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_delete_client(client, dish):
    response = client.delete(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT