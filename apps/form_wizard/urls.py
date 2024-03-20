from django.urls import path
from .views import FormWizardView


urlpatterns = [
    path(
        "form/wizard_numbered/",
        FormWizardView.as_view(template_name="form_wizard_numbered.html"),
        name="form-wizard-numbered",
    ),
    path(
        "form/wizard_icons/",
        FormWizardView.as_view(template_name="form_wizard_icons.html"),
        name="form-wizard-icons",
    ),
]
