from django.urls import path
from .views import FormsView


urlpatterns = [
    path(
        "forms/basic_inputs/",
        FormsView.as_view(template_name="forms_basic_inputs.html"),
        name="forms-basic-inputs",
    ),
    path(
        "forms/input_groups/",
        FormsView.as_view(template_name="forms_input_groups.html"),
        name="forms-input-groups",
    ),
    path(
        "forms/custom_options/",
        FormsView.as_view(template_name="forms_custom_options.html"),
        name="forms-custom-options",
    ),
    path(
        "forms/editors/",
        FormsView.as_view(template_name="forms_editors.html"),
        name="forms-editors",
    ),
    path(
        "forms/file_upload/",
        FormsView.as_view(template_name="forms_file_upload.html"),
        name="forms-file-upload",
    ),
    path(
        "forms/pickers/",
        FormsView.as_view(template_name="forms_pickers.html"),
        name="forms-pickers",
    ),
    path(
        "forms/selects/",
        FormsView.as_view(template_name="forms_selects.html"),
        name="forms-selects",
    ),
    path(
        "forms/sliders/",
        FormsView.as_view(template_name="forms_sliders.html"),
        name="forms-sliders",
    ),
    path(
        "forms/switches/",
        FormsView.as_view(template_name="forms_switches.html"),
        name="forms-switches",
    ),
    path(
        "forms/extras/",
        FormsView.as_view(template_name="forms_extras.html"),
        name="forms-extras",
    ),
]
