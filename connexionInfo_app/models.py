from django.db import models


class ConnexionInfo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    last_connexion_date = models.DateTimeField(auto_now=True)
    

# Informations de connexion:
    #     Date de création du compte
    #     Dernière connexion
    #     Historique des connexions (IP, navigateur, appareil)