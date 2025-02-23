from django.db import models
from django.conf import settings

from chat_app.models import Chat
from Player.models import Player
from localisation_app.models import Address
from sport_app.models import Sport

from django.db import models



class ProposedDate(models.Model):
    date = models.DateField()  # Date proposée
    time_slot = models.CharField(max_length=50)  # Créneau horaire
    is_preferred = models.BooleanField(default=False)  # Indique si la date est privilégiée

    def __str__(self):
        return f"{self.date} ({self.time_slot})"

class Invitation(models.Model):
    
    STATUS_CHOICES = [
    ('Pending', 'En attente'),
    ('Accepted', 'Acceptée'),
    ('Declined', 'Refusée'),
    ('Cancelled', 'Annulée'),
    ('Expired', 'Expirée'),
    ]
        
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
        max_length=20, choices=STATUS_CHOICES, blank=True, null=True
    )  # Statut de l'invitation
    message = models.TextField(null=True, blank=True)  # Message personnalisé
    proposed_location = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="proposed_invitations"
    )  # Lieu proposé
    alternative_locations = models.ManyToManyField(
        Address, blank=True, related_name="alternative_invitations"
    )  # Lieux alternatifs
    proposed_dates = models.ManyToManyField(ProposedDate, blank=True)  # Dates proposées
    confirmed_date = models.DateTimeField(null=True, blank=True)  # Date confirmée
    confirmed_location = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="confirmed_invitations"
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
