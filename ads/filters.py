import django_filters
from .models import Ad


class AdFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    author_email = django_filters.CharFilter(field_name='author__email', lookup_expr='iexact')

    class Meta:
        model = Ad
        fields = ['status', 'min_price', 'max_price', 'author_email']