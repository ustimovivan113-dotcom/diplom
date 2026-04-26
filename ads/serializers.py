from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_email = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'author_email', 'ad', 'created_at', 'updated_at']
        read_only_fields = ['author', 'ad']


class AdSerializer(serializers.ModelSerializer):
    author_email = serializers.ReadOnlyField(source='author.email')
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = [
            'id', 'title', 'price', 'description', 'author', 'author_email',
            'image', 'status', 'created_at', 'updated_at', 'comments_count'
        ]
        read_only_fields = ['author']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть больше 0')
        return value


class AdDetailSerializer(AdSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta(AdSerializer.Meta):
        fields = AdSerializer.Meta.fields + ['comments']