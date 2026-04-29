from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    """Публичная информация о пользователе."""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'image']


class UserSerializer(serializers.ModelSerializer):
    """Полная информация о пользователе (для владельца)."""
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'role', 'image']
        read_only_fields = ['role']


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'image']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)