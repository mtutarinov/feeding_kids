import pytest
from rest_framework import status

from tests.conftest import client


@pytest.mark.django_db
def test_dish_rating_client(client, dish):
    response_a = client.post(f"/api/v1/rating/{dish.id}/")
    assert response_a.status_code == status.HTTP_200_OK
    assert response_a.data['response'] == "Dish rating 1"
    response_b = client.post(f"/api/v1/rating/{dish.id}/")
    assert response_b.status_code == status.HTTP_200_OK
    assert response_b.data['response'] == "Dish rating 0"