# views.py
from rest_framework import generics
from profile_app.models import ProfileUser
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Vue pour lister tous les profils et en créer un nouveau
class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # L'utilisateur doit être authentifié pour créer/lister un profil

    def perform_create(self, serializer):
        # On attribue l'utilisateur connecté au profil créé
        serializer.save(user=self.request.user)

# Vue pour récupérer, mettre à jour et supprimer un profil spécifique
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # L'utilisateur doit être authentifié

    def get_queryset(self):
        # Limite l'accès aux profils de l'utilisateur connecté ou au profil demandé par ID
        return ProfileUser.objects.filter(user=self.request.user)
