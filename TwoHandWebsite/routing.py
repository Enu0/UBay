from django.urls import re_path
from app01 import consumers

websocket_urlpatterns = [
    # url和处理器其url的类
    re_path(r'websocket', consumers.ChatConsumer.as_asgi()),

]