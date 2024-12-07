import pytest
from rest_framework import status

from faker_food import ingredients
from food.models import Ingredient, Dish
from tests.conftest import ingredient
from tests.factories import IngredientFactory, DishFactory

INGREDIENT_LIST_URL = '/api/v1/ingredients/'
DISH_LIST_URL = '/api/v1/dishes/'


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
def test_ingredients_put_anon_client(client, ingredient):
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
def test_ingredients_patch_anon_client(client, ingredient):
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
def test_ingredients_delete_anon_client(client, ingredient):
    response = client.delete(INGREDIENT_LIST_URL + f'{ingredient.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


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
    assert len(response.data) == 3
    assert response.data['name'] == dish.name
    assert len(response.data['ingredients']) == len(ingredients) == 2
    assert response.data['ingredients'] == [ingredient.id for ingredient in ingredients]
    assert response.data['recipe'] == dish.recipe


@pytest.mark.django_db
def test_dishes_post_client(client):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test'
    }
    response = client.post(DISH_LIST_URL, data=data)
    dish = Dish.objects.get(id=response.data.serializer.instance.id)
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 3
    assert response.data['name'] == dish.name == 'test'
    assert len(response.data['ingredients']) == len(ingredients) == dish.ingredients.count() == 2
    assert response.data['ingredients'] == ingredients == [ingredient.id for ingredient in dish.ingredients.all()]
    assert response.data['recipe'] == dish.recipe == 'test'


@pytest.mark.django_db
def test_dishes_post_anon_client(anon_client):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test'
    }
    response = anon_client.post(DISH_LIST_URL, data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_put_anon_client(anon_client, dish):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test'
    }
    response = anon_client.put(DISH_LIST_URL + f'{dish.id}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_put_client(client, dish):
    ingredients = [ingredient.id for ingredient in IngredientFactory.create_batch(2)]
    data = {
        'name': 'test',
        'ingredients': ingredients,
        'recipe': 'test'
    }
    response = client.put(DISH_LIST_URL + f'{dish.id}/', data=data)
    assert response.status_code == status.HTTP_200_OK
    dish.refresh_from_db()
    assert len(response.data) == 3
    assert response.data['name'] == dish.name == 'test'
    assert len(response.data['ingredients']) == len(ingredients) == dish.ingredients.count() == 2
    assert response.data['ingredients'] == ingredients == [ingredient.id for ingredient in dish.ingredients.all()]
    assert response.data['recipe'] == dish.recipe == 'test'


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
    assert len(response.data) == 3
    assert response.data['name'] == dish.name == 'test'


@pytest.mark.django_db
def test_dishes_delete_anon_client(anon_client, dish):
    response = anon_client.delete(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dishes_delete_client(client, dish):
    response = client.delete(DISH_LIST_URL + f'{dish.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_dish_rating_anon_client(client, dish):
    response_a = client.post(f"/api/v1/rating/{dish.id}/")
    assert response_a.status_code == status.HTTP_200_OK
    assert response_a.data['response'] == "Dish rating 1"
    response_b = client.post(f"/api/v1/rating/{dish.id}/")
    assert response_b.status_code == status.HTTP_200_OK
    assert response_b.data['response'] == "Dish rating 0"