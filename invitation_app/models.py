from django.db import models
from django.conf import settings

from chat_app.models import Chat
from sport_app.models import Sport

from django.db import models

class GeoCoordinates(models.Model):
    latitude = models.FloatField()  # Latitude
    longitude = models.FloatField()  # Longitude

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

class Sport(models.Model):
    name = models.CharField(max_length=255)  # Nom du sport
    description = models.TextField(null=True, blank=True)  # Description du sport
    popularity_rank = models.IntegerField()  # Classement de popularité

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)  # Nom du lieu
    address = models.TextField()  # Adresse
    city = models.CharField(max_length=100)  # Ville
    country = models.CharField(max_length=100)  # Pays
    coordinates = models.OneToOneField(
        GeoCoordinates, on_delete=models.CASCADE, null=True, blank=True
    )  # Coordonnées géographiques
    description = models.TextField(null=True, blank=True)  # Description ou détails
    is_indoor = models.BooleanField(default=False)  # Indique si le lieu est en intérieur
    capacity = models.IntegerField(null=True, blank=True)  # Capacité maximale

    def __str__(self):
        return self.name

class Player(models.Model):
    full_name = models.CharField(max_length=255)  # Nom complet
    email = models.EmailField(unique=True)  # Adresse e-mail
    phone_number = models.CharField(max_length=20, null=True, blank=True)  # Numéro de téléphone
    date_of_birth = models.DateField()  # Date de naissance
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])  # Genre
    sports = models.ManyToManyField(Sport, related_name="players")  # Sports pratiqués

    def __str__(self):
        return self.full_name

class ProposedDate(models.Model):
    date = models.DateField()  # Date proposée
    time_slot = models.CharField(max_length=50)  # Créneau horaire
    is_preferred = models.BooleanField(default=False)  # Indique si la date est privilégiée

    def __str__(self):
        return f"{self.date} ({self.time_slot})"

class InvitationStatus(models.TextChoices):
    PENDING = 'Pending', 'En attente'
    ACCEPTED = 'Accepted', 'Acceptée'
    DECLINED = 'Declined', 'Refusée'
    CANCELLED = 'Cancelled', 'Annulée'
    EXPIRED = 'Expired', 'Expirée'

class Invitation(models.Model):
    player_a = models.ForeignKey(
        Player, related_name="sent_invitations", on_delete=models.CASCADE
    )  # Joueur A (envoyeur)
    player_b = models.ForeignKey(
        Player, related_name="received_invitations", on_delete=models.CASCADE
    )  # Joueur B (destinataire)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)  # Sport pratiqué
    invitation_date = models.DateTimeField(auto_now_add=True)  # Date d'envoi
    expiry_date = models.DateTimeField(null=True, blank=True)  # Date d'expiration
    response_date = models.DateTimeField(null=True, blank=True)  # Date de réponse
    status = models.CharField(
        max_length=20, choices=InvitationStatus.choices, default=InvitationStatus.PENDING
    )  # Statut de l'invitation
    message = models.TextField(null=True, blank=True)  # Message personnalisé
    proposed_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="proposed_invitations"
    )  # Lieu proposé
    alternative_locations = models.ManyToManyField(
        Location, blank=True, related_name="alternative_invitations"
    )  # Lieux alternatifs
    proposed_dates = models.ManyToManyField(ProposedDate, blank=True)  # Dates proposées
    confirmed_date = models.DateTimeField(null=True, blank=True)  # Date confirmée
    confirmed_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="confirmed_invitations"
    )  # Lieu confirmé
    has_players_met_before = models.BooleanField(default=False)  # Indique si les joueurs se sont rencontrés

    def __str__(self):
        return f"Invitation from {self.player_a} to {self.player_b}"

class InvitationNote(models.Model):
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()  # Contenu de la note
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return f"Note for Invitation {self.invitation.id}"
