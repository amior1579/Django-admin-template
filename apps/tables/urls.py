from django.urls import path
from .views import TableView


urlpatterns = [
    path(
        "tables/basic/",
        TableView.as_view(template_name="tables_basic.html"),
        name="tables-basic",
    ),
    path(
        "tables/datatables_basic/",
        TableView.as_view(template_name="tables_datatables_basic.html"),
        name="tables-datatables-basic",
    ),
    path(
        "tables/datatables_advanced/",
        TableView.as_view(template_name="tables_datatables_advanced.html"),
        name="tables-datatables-advanced",
    ),
    path(
        "tables/datatables_extensions/",
        TableView.as_view(template_name="tables_datatables_extensions.html"),
        name="tables-datatables-extensions",
    ),
]
