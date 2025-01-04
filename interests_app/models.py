from django.db import models
from django.conf import settings

class Interest(models.Model):
    name = models.CharField(max_length=200)

class UserInterest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)