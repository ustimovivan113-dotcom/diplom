from rest_framework import serializers
from .models import Ad, Comment
from users.serializers import UserPublicSerializer


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментария."""
    author_name = serializers.CharField(source='author.first_name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'author_name', 'ad', 'created_at']
        read_only_fields = ['author', 'ad']


class AdSerializer(serializers.ModelSerializer):
    """Базовый сериализатор объявления (список)."""
    author = UserPublicSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'image', 'status', 'created_at']


class AdDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор объявления с комментариями."""
    author = UserPublicSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'image', 'status', 'created_at', 'updated_at', 'comments']