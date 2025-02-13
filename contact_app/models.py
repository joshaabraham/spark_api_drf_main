from django.db import models

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        
    def save(self, *args, **kwargs):
        if self.user_from == self.user_to:
            raise ValueError("user_from and user_to cannot be the same ProfileUser.")
        super().save(*args, **kwargs)
