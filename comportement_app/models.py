from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

class ContentType(models.TextChoices):
    VIDEO = 'VIDEO', 'Video'
    IMAGE = 'IMAGE', 'Image'
    ARTICLE = 'ARTICLE', 'Article'
    ADVERTISEMENT = 'ADVERTISEMENT', 'Advertisement'

class UserAction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=200) # par exemple 'click', 'reaction'
    timestamp = models.DateTimeField(auto_now_add=True)
    session_duration = models.DurationField()  # durée de la session en secondes
    time_of_day = models.TimeField()  # heure de la journée
    content_type = models.CharField(max_length=20, choices=ContentType.choices)  # type de contenu
    content_id = models.PositiveIntegerField()  # ID du contenu consommé
    reaction_to_ad = models.BooleanField()  # si l'action était une réaction à une publicité