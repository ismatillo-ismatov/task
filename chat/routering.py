from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    # path("ws/",consumers.UserConsumer,as_asgi()),
    # path("ws/chat/",consumers.RoomConsumer.as_asgi())
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]