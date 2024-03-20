from django.urls import path
from .views import IconsView


urlpatterns = [
    path(
        "icons/tabler/",
        IconsView.as_view(template_name="icons_tabler.html"),
        name="icons-tabler",
    ),
    path(
        "icons/font_awesome/",
        IconsView.as_view(template_name="icons_font_awesome.html"),
        name="icons-font-awesome",
    ),
]
