import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ads.models import Ad, Comment

User = get_user_model()


def pytest_configure():
    from django.conf import settings
    settings.ROOT_URLCONF = 'config.urls'


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="user@example.com",
        first_name="Иван",
        last_name="Иванов",
        phone="+79161234567",
        password="password123"
    )

@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        email="admin@example.com",
        first_name="Админ",
        last_name="Админов",
        phone="+79167654321",
        password="admin123"
    )

@pytest.fixture
def ad(db, user):
    return Ad.objects.create(
        title="Продаю iPhone 13",
        price=75000,
        description="Отличный телефон в хорошем состоянии",
        author=user,
        status="active"
    )

@pytest.fixture
def comment(db, ad, user):
    return Comment.objects.create(
        text="Сколько проработал аккумулятор?",
        author=user,
        ad=ad
    )

@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def admin_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client