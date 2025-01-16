import pytest
from rest_framework import status

from tests.factories import AllergenFactory, ChildFactory, UserFactory


@pytest.mark.django_db
def test_allergen_list_anon_client(anon_client, child):
    AllergenFactory.create(child=child)
    response = anon_client.get(f"/api/v1/child/{child.id}/allergens/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_allergen_list_client(client, child):
    AllergenFactory.create(child=child)
    response = client.get(f"/api/v1/child/{child.id}/allergens/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_allergen_list_not_allowed_user(client, ingredient):
    user = UserFactory.create()
    child = ChildFactory.create(mother=user)
    AllergenFactory.create(child=child, ingredient=ingredient)
    response = client.get(f"/api/v1/child/{child.id}/allergens/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert (
        response.data["detail"]
        == "Вы можете просматривать аллергены только своих детей."
    )


@pytest.mark.django_db
def test_allergen_post_anon_client(anon_client, child, ingredient):
    data = {"child": child.id, "ingredient": ingredient.id}
    response = anon_client.post(f"/api/v1/child/{child.id}/allergens/", data=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_allergen_post_client(client, ingredient):
    child = ChildFactory.create(mother=client.user)
    data = {"child": child.id, "ingredient": ingredient.id}
    response = client.post(f"/api/v1/child/{child.id}/allergens/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 3
    assert response.data["child"] == child.id
    assert response.data["ingredient"] == ingredient.id


@pytest.mark.django_db
def test_allergen_post_not_allowed_user(client, ingredient):
    user = UserFactory.create()
    child = ChildFactory.create(mother=user)
    data = {"child": child.id, "ingredient": ingredient.id}
    response = client.post(f"/api/v1/child/{child.id}/allergens/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert (
        response.data["detail"]
        == "Вы можете создавать аллергены только для своих детей."
    )


@pytest.mark.django_db
def test_allergen_put_anon_client(anon_client, allergen, child, ingredient):
    data = {"child": child.id, "ingredient": ingredient.id}
    response = anon_client.put(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_allergen_put_client(client, allergen, child, ingredient):
    data = {"child": child.id, "ingredient": ingredient.id}
    response = client.put(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    assert response.data["child"] == data["child"] == child.id
    assert response.data["ingredient"] == data["ingredient"] == ingredient.id


@pytest.mark.django_db
def test_allergen_put_not_allowed_user(client, ingredient):
    user = UserFactory.create()
    child = ChildFactory.create(mother=user)
    allergen = AllergenFactory.create(child=child, ingredient=ingredient)
    data = {"child": child.id, "ingredient": ingredient.id}
    response = client.put(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data["detail"] == "Вы можете изменять аллергены только своих детей"


@pytest.mark.django_db
def test_allergen_patch_anon_client(anon_client, allergen, child, ingredient):
    data = {"ingredient": ingredient.id}
    response = anon_client.patch(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_allergen_patch_client(client, allergen, child, ingredient):
    data = {"ingredient": ingredient.id}
    response = client.patch(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    assert response.data["child"] == child.id
    assert response.data["ingredient"] == data["ingredient"] == ingredient.id


@pytest.mark.django_db
def test_allergen_patch_not_allowed_user(client, ingredient):
    user = UserFactory.create()
    child = ChildFactory.create(mother=user)
    allergen = AllergenFactory.create(child=child, ingredient=ingredient)
    data = {"ingredient": ingredient.id}
    response = client.patch(
        f"/api/v1/child/{child.id}/allergens/{allergen.id}/", data=data
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data["detail"] == "Вы можете изменять аллергены только своих детей"


@pytest.mark.django_db
def test_allergen_delete_anon_client(anon_client, allergen, child):
    response = anon_client.delete(f"/api/v1/child/{child.id}/allergens/{allergen.id}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_allergen_delete_client(client, allergen, child):
    response = client.delete(f"/api/v1/child/{child.id}/allergens/{allergen.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_allergen_delete_not_allowed_user(client, ingredient):
    user = UserFactory.create()
    child = ChildFactory.create(mother=user)
    allergen = AllergenFactory.create(child=child, ingredient=ingredient)
    response = client.delete(f"/api/v1/child/{child.id}/allergens/{allergen.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data["detail"] == "Вы можете удалять аллергены только своих детей."
