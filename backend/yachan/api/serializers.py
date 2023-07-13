from rest_framework.serializers import ModelSerializer

from .models import Category, ThreadModel, Post


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ThreadSerializer(ModelSerializer):
    class Meta:
        model = ThreadModel
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
