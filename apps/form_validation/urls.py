from django.urls import path
from .views import FormValidationView


urlpatterns = [
    path(
        "form/validation/",
        FormValidationView.as_view(template_name="form_validation.html"),
        name="form-validation",
    ),
]
