from django.urls import path
from .views import ChartsView


urlpatterns = [
    path(
        "charts/apex/",
        ChartsView.as_view(template_name="charts_apex.html"),
        name="charts-apex",
    ),
    path(
        "charts/chartjs/",
        ChartsView.as_view(template_name="charts_chartjs.html"),
        name="charts-chartjs",
    ),
]
