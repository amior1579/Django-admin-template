from django.urls import path
from .views import MapView


urlpatterns = [
    path(
        "maps/leaflet/",
        MapView.as_view(template_name="maps_leaflet.html"),
        name="maps-leaflet",
    ),
]
