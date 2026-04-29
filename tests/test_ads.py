import pytest
from rest_framework import status
from ads.models import Ad
from users.models import User


@pytest.mark.django_db
def test_list_ads(api_client, ad):
    url = "/api/ads/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    if isinstance(response.data, list):
        assert len(response.data) >= 1
    else:
        assert len(response.data['results']) >= 1


@pytest.mark.django_db
def test_create_ad_authenticated(authenticated_client, user):
    url = "/api/ads/"
    data = {
        "title": "Продаю ноутбук",
        "price": 45000,
        "description": "Хороший ноутбук для работы",
        "status": "active"
    }
    response = authenticated_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "Продаю ноутбук"
    assert response.data["author"]["id"] == user.id


@pytest.mark.django_db
def test_create_ad_unauthenticated(api_client):
    url = "/api/ads/"
    data = {"title": "Тест", "price": 1000, "description": "Описание"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_retrieve_ad(api_client, ad):
    url = f"/api/ads/{ad.pk}/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == ad.pk
    assert response.data["title"] == ad.title


@pytest.mark.django_db
def test_update_own_ad(authenticated_client, ad):
    url = f"/api/ads/{ad.pk}/"
    data = {"title": "Обновлённое название", "price": 80000}
    response = authenticated_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Обновлённое название"


@pytest.mark.django_db
def test_update_foreign_ad(authenticated_client, admin_user):
    other_user = User.objects.create_user(
        email="other@example.com",
        first_name="Другой",
        last_name="Пользователь",
        phone="+79160000000",
        password="pass123"
    )
    foreign_ad = Ad.objects.create(
        title="Чужое объявление",
        price=10000,
        description="Описание",
        author=other_user
    )
    url = f"/api/ads/{foreign_ad.pk}/"
    data = {"title": "Попытка изменить чужое"}
    response = authenticated_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_own_ad(authenticated_client, ad):
    url = f"/api/ads/{ad.pk}/"
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Ad.objects.filter(pk=ad.pk).exists()


@pytest.mark.django_db
def test_filter_ads_by_price(api_client, ad):
    url = "/api/ads/?min_price=70000&max_price=80000"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_search_ads(api_client, ad):
    url = "/api/ads/?search=iPhone"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK