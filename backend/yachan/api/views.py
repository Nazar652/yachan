from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import *

from .serializers import *
from .signals import PollingHandler


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ThreadViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def polling_handling(request):
    while True:
        if PollingHandler.new_thread:
            PollingHandler.new_thread = False
            break
        if PollingHandler.new_post:
            PollingHandler.new_post = False
            break
        if PollingHandler.update_post:
            PollingHandler.update_post = False
            break

    return Response({})
