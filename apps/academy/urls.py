from django.urls import path
from .views import AcademyView


urlpatterns = [
    path(
        "app/academy/dashboard/",
        AcademyView.as_view(template_name="app_academy_dashboard.html"),
        name="app-academy-dashboard",
    ),
    path(
        "app/academy/course/",
        AcademyView.as_view(template_name="app_academy_course.html"),
        name="app-academy-course",
    ),
    path(
        "app/academy/course_details/",
        AcademyView.as_view(template_name="app_academy_course_details.html"),
        name="app-academy-course-details",
    ),
]
