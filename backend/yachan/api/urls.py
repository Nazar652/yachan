from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
