from django.contrib import admin
from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'author', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description', 'author__email']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'ad', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'author__email', 'ad__title']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']