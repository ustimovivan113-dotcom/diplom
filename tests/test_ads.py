import pytest
from django.urls import reverse
from rest_framework import status
from ads.models import Ad
from users.models import User


@pytest.mark.django_db
def test_list_ads(api_client, ad):
    """Тест получения списка объявлений (доступно всем)"""
    url = reverse('ad-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    # Поддерживаем как пагинированный ответ (словарь с results), так и обычный список
    if isinstance(response.data, list):
        assert len(response.data) >= 1
    else:
        assert len(response.data['results']) >= 1


@pytest.mark.django_db
def test_create_ad_authenticated(authenticated_client, user):
    """Тест создания объявления авторизованным пользователем"""
    url = reverse('ad-list')
    data = {
        'title': 'Продаю ноутбук',
        'price': 45000,
        'description': 'Хороший ноутбук для работы',
        'status': 'active'
    }
    response = authenticated_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'Продаю ноутбук'
    assert response.data['author'] == user.id


@pytest.mark.django_db
def test_create_ad_unauthenticated(api_client):
    """Тест попытки создания объявления без авторизации"""
    url = reverse('ad-list')
    data = {
        'title': 'Тест',
        'price': 1000,
        'description': 'Описание'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_retrieve_ad(api_client, ad):
    """Тест получения детальной информации об объявлении"""
    url = reverse('ad-detail', kwargs={'pk': ad.pk})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == ad.pk
    assert response.data['title'] == ad.title


@pytest.mark.django_db
def test_update_own_ad(authenticated_client, ad):
    """Тест обновления своего объявления"""
    url = reverse('ad-detail', kwargs={'pk': ad.pk})
    data = {'title': 'Обновлённое название', 'price': 80000}
    response = authenticated_client.patch(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Обновлённое название'


@pytest.mark.django_db
def test_update_foreign_ad(authenticated_client, admin_user):
    """Тест попытки обновить чужое объявление (должен быть 403)"""
    other_user = User.objects.create_user(
        email="other@example.com",
        first_name="Другой",
        last_name="Пользователь",
        phone="+79160000000",          # ← обязательно
        password="pass123"
    )
    foreign_ad = Ad.objects.create(
        title="Чужое объявление",
        price=10000,
        description="Описание",
        author=other_user
    )

    url = reverse('ad-detail', kwargs={'pk': foreign_ad.pk})
    data = {'title': 'Попытка изменить чужое'}
    response = authenticated_client.patch(url, data, format='json')

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_own_ad(authenticated_client, ad):
    """Тест удаления своего объявления"""
    url = reverse('ad-detail', kwargs={'pk': ad.pk})
    response = authenticated_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Ad.objects.filter(pk=ad.pk).exists()


@pytest.mark.django_db
def test_filter_ads_by_price(api_client, ad):
    """Тест фильтрации по цене"""
    url = reverse('ad-list') + '?min_price=70000&max_price=80000'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_search_ads(api_client, ad):
    """Тест поиска по названию/описанию"""
    url = reverse('ad-list') + '?search=iPhone'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK