from django.urls import path
from .views import InvitationListCreateView, InvitationRetrieveUpdateDestroyView

urlpatterns = [
    path('invitationCreate/', InvitationListCreateView.as_view(), name='invitations_create'),
    path('invitation/<int:pk>/', InvitationRetrieveUpdateDestroyView.as_view(), name='invitations_retrieve_update_destroy'),
]