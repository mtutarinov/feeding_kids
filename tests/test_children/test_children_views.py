import pytest
from rest_framework import status
from django.contrib.auth.models import User

from children.models import Child
from tests.factories import UserFactory, ChildFactory

CHILDREN_LIST_URL = "/api/v1/children/"


@pytest.mark.django_db
def test_children_get_list_anon_client(anon_client):
    response = anon_client.get(CHILDREN_LIST_URL)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_children_get_list_client(client):
    response = client.get(CHILDREN_LIST_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Child.objects.count()


@pytest.mark.django_db
def test_children_get_detail_anon_client(anon_client, child):
    response = anon_client.get(CHILDREN_LIST_URL + f'{child.uuid}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_children_get_detail_client(client, child):
    response = client.get(CHILDREN_LIST_URL + f'{child.uuid}/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5
    assert response.data['uuid'] == str(child.uuid)
    assert response.data['name'] == child.name
    assert response.data['age'] == child.age
    assert response.data['months'] == child.months
    assert response.data['mother'] == child.mother.id


@pytest.mark.django_db
def test_children_post_anon_client(anon_client, user):
    data = {
        "name": "test",
        "age": 1,
        "months": 2,
        "mother": user.id
    }

    response = anon_client.post(CHILDREN_LIST_URL, data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_children_post_client(client, user):
    data = {
        "name": "test",
        "age": 1,
        "months": 2,
        "mother": user.id
    }

    response = client.post(CHILDREN_LIST_URL, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    child = Child.objects.get(uuid=response.data['uuid'])
    assert len(response.data) == 5
    assert response.data['name'] == child.name == 'test'
    assert response.data['age'] == child.age == 1
    assert response.data['months'] == child.months == 2
    assert response.data['mother'] == child.mother.id == user.id


@pytest.mark.django_db
def test_children_put_anon_client(anon_client, child):
    data = {
        "name": "test",
    }
    response = anon_client.put(CHILDREN_LIST_URL + f'{child.uuid}/', data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_children_put_client(client, child, user):
    data = {
        "name": "test",
        "mother": user.id
    }
    response = client.put(CHILDREN_LIST_URL + f'{child.uuid}/', data=data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_children_delete_anon_client(anon_client, child):
    response = anon_client.delete(CHILDREN_LIST_URL + f'{child.uuid}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_children_delete_client(client, child):
    response = client.delete(CHILDREN_LIST_URL + f'{child.uuid}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
