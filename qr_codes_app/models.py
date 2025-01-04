from django.db import models

class QRCode(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]