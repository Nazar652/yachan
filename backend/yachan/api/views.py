from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Category, ThreadModel, Post
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer


class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CategoryListAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ThreadDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class ThreadListAPI(ListCreateAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
