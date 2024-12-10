import pytest
from rest_framework import status

from tests.conftest import anon_client, client


DISH_CHOSEN = '/api/v1/chosen/'

@pytest.mark.django_db
def test_dish_chosen_detail_anon_client(anon_client):
    response = anon_client.get(DISH_CHOSEN)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dish_chosen_detail_client(client):
    response = client.get(DISH_CHOSEN)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['chosen']) == 2
    assert response.data['chosen']['user'] == client.user.id
    assert len(response.data['chosen']['dish']) == 0
    assert response.data['chosen']['dish'] == []


@pytest.mark.django_db
def test_dish_chosen_put_anon_client(anon_client, dish):
    response = anon_client.put(DISH_CHOSEN + f'{dish.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dish_chosen_put_client(client, dish):
    response = client.put(DISH_CHOSEN + f'{dish.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['chosen']) == 2
    assert response.data['chosen']['user'] == client.user.id
    assert len(response.data['chosen']['dish']) == 1
    assert response.data['chosen']['dish'] == [dish.id]