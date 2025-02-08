from django.urls import path
from .views import UserComportementListCreateView, UserComportementRetrieveUpdateDestroyView

urlpatterns = [
    path('useractionCreate/', UserComportementListCreateView.as_view(), name='useractions_create'),
    path('useraction/<int:pk>/', UserComportementRetrieveUpdateDestroyView.as_view(), name='useraction_retrieve_update_destroy'),
]