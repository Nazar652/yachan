from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('csrf/', get_csrf_token),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('check-authentication/', check_authentication, name='check_authentication')
]
