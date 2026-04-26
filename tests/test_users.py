import pytest
from django.urls import reverse
from rest_framework import status
from users.models import User


@pytest.mark.django_db
def test_register_user(api_client):
    """Тест успешной регистрации"""
    url = reverse('register')
    data = {
        'email': 'newuser@example.com',
        'password': 'StrongPass123',
        'first_name': 'Новый',
        'last_name': 'Пользователь',
        'phone': '+79161234567'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['email'] == 'newuser@example.com'


@pytest.mark.django_db
def test_register_duplicate_email(api_client, user):
    """Тест регистрации с уже существующим email (используем фикстуру user)"""
    url = reverse('register')
    data = {
        'email': user.email,
        'password': 'StrongPass123',
        'first_name': 'Тест',
        'last_name': 'Тестов',
        'phone': '+79161234567'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_own_profile(authenticated_client, user):
    """Тест получения своего профиля"""
    url = reverse('user-profile')
    response = authenticated_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == user.email


@pytest.mark.django_db
def test_update_profile(authenticated_client, user):
    """Тест обновления профиля"""
    url = reverse('user-profile')
    data = {
        'first_name': 'НовоеИмя',
        'phone': '+79998887766'
    }
    response = authenticated_client.patch(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['first_name'] == 'НовоеИмя'


@pytest.mark.django_db
def test_jwt_login(api_client, user):
    """Тест получения JWT токена"""
    url = reverse('token-obtain-pair')
    data = {
        'email': user.email,
        'password': 'password123'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_unauthorized_profile(api_client):
    """Тест доступа к профилю без авторизации"""
    url = reverse('user-profile')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED