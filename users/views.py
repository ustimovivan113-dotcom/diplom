from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    """Регистрация нового пользователя."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Просмотр и редактирование профиля текущего пользователя."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user