from django.urls import path
from .views import GeocodeView, ReverseGeocodeView, AddressListCreateView, AddressRetrieveUpdateDestroyView

urlpatterns = [
    
    path('geocode/', GeocodeView.as_view(), name='geocode'),
    path('reverse-geocode/', ReverseGeocodeView.as_view(), name='reverse_geocode'),
    
    path("addresses/", AddressListCreateView.as_view(), name="address_list_create"),
    path("addresses/<int:pk>/", AddressRetrieveUpdateDestroyView.as_view(), name="address_detail"),
]