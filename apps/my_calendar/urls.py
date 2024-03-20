from django.urls import path
from .views import CalendarView


urlpatterns = [
    path(
        "app/calendar/",
        CalendarView.as_view(template_name="app_calendar.html"),
        name="app-calendar",
    ),
]
