from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение: только владелец или администратор может редактировать/удалять.
    Просмотр разрешен всем.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Проверяем, является ли пользователь автором или админом
        return obj.author == request.user or request.user.role == 'admin'
