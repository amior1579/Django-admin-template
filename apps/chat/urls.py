from django.urls import path
from .views import ChatView


urlpatterns = [
    path(
        "app/chat/",
        ChatView.as_view(template_name="app_chat.html"),
        name="app-chat",
    ),
]
