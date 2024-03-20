from django.urls import path
from .views import EmailView


urlpatterns = [
    path(
        "app/email/",
        EmailView.as_view(template_name="app_email.html"),
        name="app-email",
    ),
]
