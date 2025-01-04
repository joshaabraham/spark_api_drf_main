from django.db import models
from django.conf import settings

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="member_profile")
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class SportEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Promotion(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.code


class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    sport_event = models.ForeignKey(SportEvent, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.member.user.username} - {self.sport_event.name}"
