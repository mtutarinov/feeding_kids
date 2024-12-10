import pytest
from rest_framework import status

from tests.conftest import anon_client, client

DISH_HISTORY = '/api/v1/history/'


@pytest.mark.django_db
def test_dish_history_detail_anon_client(anon_client):
    response = anon_client.get(DISH_HISTORY)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dish_history_detail_client(client):
    response = client.get(DISH_HISTORY)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['history']) == 2
    assert response.data['history']['user'] == client.user.id
    assert len(response.data['history']['dish']) == 0
    assert response.data['history']['dish'] == []


@pytest.mark.django_db
def test_dish_history_put_anon_client(anon_client, dish):
    response = anon_client.put(DISH_HISTORY + f'{dish.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_dish_history_put_client(client, dish):
    response = client.put(DISH_HISTORY + f'{dish.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['history']) == 2
    assert response.data['history']['user'] == client.user.id
    assert len(response.data['history']['dish']) == 1
    assert response.data['history']['dish'] == [dish.id]
