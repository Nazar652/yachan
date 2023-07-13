from django.conf.urls.static import static
from django.urls import path

from yachan import settings
from .views import *


urlpatterns = [
    path('categories/', CategoryListAPI.as_view()),
    path('categories/<slug:slug>/', CategoryDetailAPI.as_view()),
    path('threads/', ThreadListAPI.as_view()),
    path('threads/<int:pk>/', ThreadDetailAPI.as_view()),
    path('posts/', PostListAPI.as_view()),
    path('posts/<int:pk>/', PostDetailAPI.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
