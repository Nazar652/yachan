from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import *

from .permissions import IsAdminOrOwner
from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


@csrf_exempt
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Bad request'}, status=400)


@csrf_exempt
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)
    return JsonResponse({'error': 'Bad request'}, status=400)


@api_view(['GET'])
def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True, 'username': request.user.username}, status=200)
    else:
        return JsonResponse({'isAuthenticated': False}, status=200)


class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ThreadPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ThreadViewSet(ModelViewSet):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer
    pagination_class = ThreadPagination
    permission_classes = (IsAdminOrOwner, )

    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = (IsAdminOrOwner, )

    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
