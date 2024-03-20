from django.urls import path
from .views import LogisticsView


urlpatterns = [
    path(
        "app/logistics/dashboard/",
        LogisticsView.as_view(template_name="app_logistics_dashboard.html"),
        name="app-logistics-dashboard",
    ),
    path(
        "app/logistics/fleet/",
        LogisticsView.as_view(template_name="app_logistics_fleet.html"),
        name="app-logistics-fleet",
    ),
]
