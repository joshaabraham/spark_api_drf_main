from django.db import models

from equipe_app.models import Team
from sport_app.models import Sport

# Create your models here.
class Player(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
        ('OTH', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Height in meters", blank=True, null=True)
    weight = models.FloatField(help_text="Weight in kilograms", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="players/profile_pictures/", blank=True, null=True)
    sports = models.ManyToManyField(Sport, related_name="players")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="players", blank=True, null=True)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True, help_text="Player's notable achievements")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def bmi(self):
        """
        Calculate and return the Body Mass Index (BMI) if height and weight are provided.
        """
        if self.height and self.weight:
            return round(self.weight / (self.height ** 2), 2)
        return None

    def age(self):
        """
        Calculate and return the player's age based on their date of birth.
        """
        from datetime import date
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None