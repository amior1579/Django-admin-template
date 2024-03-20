from django.urls import path

from .views import DashboardsView


urlpatterns = [
    path(
        "",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="index",
    ),
    path(
        "dashboard/crm/",
        DashboardsView.as_view(template_name="dashboard_crm.html"),
        name="dashboard-crm",
    ),
]
