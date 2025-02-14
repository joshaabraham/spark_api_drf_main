from django.conf import settings
from django.utils import timezone
from localisation_app.models import Address
from django.db import models
from contact_app.api.serializers import User
from images_app.models import Album  # Importez le modèle AlbumPhoto

class ProfileUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    background = models.ImageField(upload_to='cover_pics/', null=True, blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', blank=True, related_name='followers_set', symmetrical=False)
    following = models.ManyToManyField('self', blank=True, related_name='following_set', symmetrical=False)
    posts_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    friends_count = models.PositiveIntegerField(default=0)
    albums_photo = models.ManyToManyField('images_app.Album', blank=True, related_name='profile_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"{self.name}"

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
