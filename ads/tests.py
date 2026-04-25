import pytest
from django.urls import reverse
from rest_framework import status
from ads.models import Ad

@pytest.mark.django_db
class TestAdsAPI:
    def test_list_ads_anonymous(self, client):
        """Тест: анонимный пользователь может видеть список объявлений."""
        url = reverse('ads-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_ad_anonymous_fails(self, client):
        """Тест: анонимный пользователь не может создать объявление."""
        url = reverse('ads-list')
        data = {
            "title": "Test Ad",
            "price": 1000,
            "description": "Test description"
        }
        response = client.get(url)
        # Verify anonymous can't POST (simple check since we only test GET above)
        response = client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
