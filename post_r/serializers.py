from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at', 'category']

