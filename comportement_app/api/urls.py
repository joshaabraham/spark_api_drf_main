from django.urls import path
from .views import UserActionListCreateView, UserActionRetrieveUpdateDestroyView

urlpatterns = [
    path('useractionCreate/', UserActionListCreateView.as_view(), name='useractions_create'),
    path('useraction/<int:pk>/', UserActionRetrieveUpdateDestroyView.as_view(), name='useraction_retrieve_update_destroy'),
]