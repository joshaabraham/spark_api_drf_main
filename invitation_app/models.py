from django.db import models
from django.conf import settings

from chat_app.models import Chat
from sport_app.models import Sport

class Invitation(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='sent_invitations', 
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='received_invitations', 
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE, 
        related_name='invitations', 
        null=True, 
        blank=True
    )
    
    invitation_chat = models.ForeignKey(Chat, related_name='invitations', on_delete=models.CASCADE, max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'receiver', 'date')