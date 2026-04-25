from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register('', AdViewSet, basename='ads')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:ad_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('<int:ad_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comments-detail'),
]
