from django.urls import path
from .views import AccessView


urlpatterns = [
    path(
        "app/access/roles/",
        AccessView.as_view(template_name="app_access_roles.html"),
        name="app-access-roles",
    ),
    path(
        "app/access/permission/",
        AccessView.as_view(template_name="app_access_permission.html"),
        name="app-access-permission",
    ),
]
