from django.db import models
from django.conf import settings


class Chat(models.Model):
    """
    Modèle pour représenter une conversation (chat).
    Peut être une conversation privée ou un groupe.
    """
    CHAT_TYPE_CHOICES = [
        ('private', 'Private'),
        ('group', 'Group'),
    ]

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="chats")
    chat_type = models.CharField(max_length=10, choices=CHAT_TYPE_CHOICES, default='private')
    name = models.CharField(max_length=255, blank=True, null=True)  # Nom du groupe (pour les chats de type "group")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.chat_type == 'private':
            return f"Private Chat {self.pk}"
        return f"Group Chat {self.name or self.pk}"


class Message(models.Model):
    """
    Modèle pour représenter un message dans un chat.
    """
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Indique si le message a été lu

    def __str__(self):
        return f"Message {self.pk} from {self.sender.username}"


class GroupInvitation(models.Model):
    """
    Modèle pour gérer les invitations à des groupes.
    """
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="invitations")
    invited_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="group_invitations")
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_invitations")
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Invitation to {self.chat.name or self.chat.pk} for {self.invited_user.username}"


class MessageStatus(models.Model):
    """
    Modèle pour suivre le statut des messages (lus/non lus) par utilisateur.
    """
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="statuses")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="message_statuses")
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Message {self.message.pk} status for {self.user.username}"
