from django.urls import path
from .views import ModalExampleView


urlpatterns = [
    path(
        "modal_examples/",
        ModalExampleView.as_view(template_name="modal_examples.html"),
        name="modal-examples",
    ),
]
