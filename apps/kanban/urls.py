from django.urls import path
from .views import KanbanView


urlpatterns = [
    path(
        "app/kanban/",
        KanbanView.as_view(template_name="app_kanban.html"),
        name="app-kanban",
    ),
]
