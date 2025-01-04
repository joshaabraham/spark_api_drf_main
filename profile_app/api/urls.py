# urls.py
from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),  # Pour lister et créer des profils
    path('profile/', UserProfileDetailView.as_view(), name='userprofile-detail'),  # Pour récupérer, mettre à jour et supprimer un profil
]
