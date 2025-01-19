from django.utils import timezone
from localisation_app.models import Address
from django.db import models

from contact_app.api.serializers import User

# Create your models here.

class ProfileUser(models.Model):
    # Relation OneToOne avec le modèle User par défaut de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Champs supplémentaires pour le profil utilisateur
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='cover_pics/', null=True, blank=True)

    # Champs relatifs à l'activité de l'utilisateur
    website = models.URLField(max_length=200, blank=True, null=True)
    is_private = models.BooleanField(default=False)

    # Champs pour la gestion des amis, abonnés et abonnements
    # friends = models.ManyToManyField('self', blank=True, related_name='friend_set', symmetrical=True)
    followers = models.ManyToManyField('self', blank=True, related_name='followers_set', symmetrical=False)
    following = models.ManyToManyField('self', blank=True, related_name='following_set', symmetrical=False)

    # Champs supplémentaires pour les données d'activité sociale
    posts_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    friends_count = models.PositiveIntegerField(default=0)

    # Informations temporelles
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s profile"

    # Méthode pour ajouter un ami
    def add_friend(self, profile):
        self.friends.add(profile)
        profile.friends.add(self)
        self.friends_count += 1
        profile.friends_count += 1
        self.save()
        profile.save()

    # Méthode pour supprimer un ami
    def remove_friend(self, profile):
        self.friends.remove(profile)
        profile.friends.remove(self)
        self.friends_count -= 1
        profile.friends_count -= 1
        self.save()
        profile.save()

    # Méthode pour suivre un utilisateur
    def follow(self, profile):
        self.following.add(profile)
        profile.followers.add(self)
        self.following_count += 1
        profile.followers_count += 1
        self.save()
        profile.save()

    # Méthode pour arrêter de suivre un utilisateur
    def unfollow(self, profile):
        self.following.remove(profile)
        profile.followers.remove(self)
        self.following_count -= 1
        profile.followers_count -= 1
        self.save()
        profile.save()

    # Méthode pour obtenir tous les amis
    def get_friends(self):
        return self.friends.all()

    # Méthode pour obtenir tous les abonnés
    def get_followers(self):
        return self.followers.all()

    # Méthode pour obtenir tous les abonnements
    def get_following(self):
        return self.following.all()
    
    
    
