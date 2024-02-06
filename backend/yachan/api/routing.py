from django.urls import path, re_path
from .consumers import CategoryConsumer, ThreadConsumer

websocket_urlpatterns = [
    re_path(r'ws/category/(?P<category>\w+)/$', CategoryConsumer.as_asgi()),
    re_path(r'ws/thread/(?P<thread_id>\w+)/$', ThreadConsumer.as_asgi()),
]
