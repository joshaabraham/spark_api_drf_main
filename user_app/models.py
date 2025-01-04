from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, password, **extra_fields):
        if not email:
            raise ValueError("L'adresse e-mail est obligatoire.")
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
        
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    co_players = models.ManyToManyField("self", blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "password"]

    def __str__(self):
        return self.username
    
    
    # Informations personnelles de base:
    #     Identifiant utilisateur (ID)
    #     Nom complet
    #     Date de naissance
    #     Genre
    #     Adresse e-mail
    #     Numéro de téléphone
    #     Photo de profil
    #     Localisation géographique

    # Informations de connexion:
    #     Date de création du compte
    #     Dernière connexion
    #     Historique des connexions (IP, navigateur, appareil)

    # Informations professionnelles et éducatives:
    #     Emploi actuel
    #     Entreprises précédentes
    #     Secteur d'activité
    #     Formation (écoles, universités, diplômes)

    # Relations et interactions:
    #     Liste d'amis / abonnés / abonnements
    #     Groupes et communautés
    #     Interactions avec les publications (likes, commentaires, partages)
    #     Messages privés
    #     Mentions et tags

    # Préférences et centres d'intérêt:
    #     Pages et comptes suivis
    #     Centres d'intérêt (musique, films, sports, etc.)
    #     Hashtags et sujets favoris
    #     Langues et préférences de contenu

    # Publications et contenu partagé:
    #     Textes, images, vidéos, liens
    #     Dates et heures de publication
    #     Engagements et statistiques (nombre de vues, likes, commentaires)

    # Paramètres de confidentialité et de sécurité:
    #     Visibilité du profil
    #     Permissions d'accès aux informations
    #     Paramètres de notification
    #     Historique des actions de modération (blocages, signalements, etc.)

    # Données comportementales et d'engagement:
    #     Temps passé sur la plateforme
    #     Types de contenu consommés
    #     Fréquence et durée des sessions
    #     Actions et réactions aux publicités