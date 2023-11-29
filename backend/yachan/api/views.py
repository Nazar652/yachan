from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import *

from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ThreadViewSet(ModelViewSet):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
