from django.urls import path
from .views import InvoiceView, InvoicePrintView


urlpatterns = [
    path(
        "app/invoice/list/",
        InvoiceView.as_view(template_name="app_invoice_list.html"),
        name="app-invoice-list",
    ),
    path(
        "app/invoice/preview/",
        InvoiceView.as_view(template_name="app_invoice_preview.html"),
        name="app-invoice-preview",
    ),
    path(
        "app/invoice/edit/",
        InvoiceView.as_view(template_name="app_invoice_edit.html"),
        name="app-invoice-edit",
    ),
    path(
        "app/invoice/add/",
        InvoiceView.as_view(template_name="app_invoice_add.html"),
        name="app-invoice-add",
    ),
    path(
        "app/invoice/print/",
        InvoicePrintView.as_view(template_name="app_invoice_print.html"),
        name="app-invoice-print",
    ),
]
