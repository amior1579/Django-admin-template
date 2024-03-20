from django.urls import path
from .views import CardView


urlpatterns = [
    path(
        "cards/basic/",
        CardView.as_view(template_name="cards_basic.html"),
        name="cards-basic",
    ),
    path(
        "cards/advance/",
        CardView.as_view(template_name="cards_advance.html"),
        name="cards-advance",
    ),
    path(
        "cards/statistics/",
        CardView.as_view(template_name="cards_statistics.html"),
        name="cards-statistics",
    ),
    path(
        "cards/analytics/",
        CardView.as_view(template_name="cards_analytics.html"),
        name="cards-analytics",
    ),
    path(
        "cards/actions/",
        CardView.as_view(template_name="cards_actions.html"),
        name="cards-actions",
    ),
]
