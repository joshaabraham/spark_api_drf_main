from django.db import models
from django.conf import settings

class UserConfiguration(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.key}"
    
    
# Paramètres de confidentialité et de sécurité:

    # Visibilité du profil
    # Permissions d'accès aux informations
    # Paramètres de notification
    # Historique des actions de modération (blocages, signalements, etc.)
