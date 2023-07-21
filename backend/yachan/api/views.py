from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Category, ThreadModel, Post, ImageModel
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer, ImageModelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ThreadViewSet(ModelViewSet):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

