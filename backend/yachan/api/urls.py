from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    # path('categories/', CategoryListAPI.as_view()),
    # path('categories/<slug:slug>/', CategoryDetailAPI.as_view()),
    # path('threads/', ThreadListAPI.as_view()),
    # path('threads/<int:pk>/', ThreadDetailAPI.as_view()),
    # path('posts/', PostListAPI.as_view()),
    # path('posts/<int:pk>/', PostDetailAPI.as_view())
    path('', include(router.urls)),
]
