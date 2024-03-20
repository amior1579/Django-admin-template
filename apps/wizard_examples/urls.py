from django.urls import path
from .views import WizardExamplesView


urlpatterns = [
    path(
        "wizard_ex/checkout/",
        WizardExamplesView.as_view(template_name="wizard_ex_checkout.html"),
        name="wizard-ex-checkout",
    ),
    path(
        "wizard_ex/property_listing/",
        WizardExamplesView.as_view(template_name="wizard_ex_property_listing.html"),
        name="wizard-ex-property-listing",
    ),
    path(
        "wizard_ex/create_deal/",
        WizardExamplesView.as_view(template_name="wizard_ex_create_deal.html"),
        name="wizard-ex-create-deal",
    ),
]
