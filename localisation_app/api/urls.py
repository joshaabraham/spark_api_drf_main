from django.urls import path
from . import views

urlpatterns = [
    path("addresses/", views.AddressListCreateView.as_view(), name="address_list_create"),
    path("addresses/<int:pk>/", views.AddressRetrieveUpdateDestroyView.as_view(), name="address_detail"),
]