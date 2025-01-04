from django.urls import path
from .views import ContactListCreateView, ContactRetrieveUpdateDestroyView

urlpatterns = [
    path('contactCreateList/', ContactListCreateView.as_view(), name='contact_create'),
    path('contact/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact_retrieve_update_destroy'),
]