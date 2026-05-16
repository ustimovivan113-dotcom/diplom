from django.db import models
from django.conf import settings


class Ad(models.Model):
    """Модель объявления."""
    STATUS_CHOICES = (
        ('active', 'Активно'),
        ('closed', 'Закрыто'),
    )

    title = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='ads',
        verbose_name='Автор'
    )
    image = models.ImageField(upload_to='ads/%Y/%m/', null=True, blank=True, verbose_name='Изображение')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментария к объявлению."""
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявление'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return f'Комментарий от {self.author.email} к {self.ad.title}'