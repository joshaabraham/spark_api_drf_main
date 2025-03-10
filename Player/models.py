from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    LEVEL_CHOICES = [
    ('TB', 'True Beginner'),
    ('BEG', 'Beginner'),
    ('INT', 'Intermediate'),
    ('ADV', 'Advanced'),
    ('EXP', 'Expert'),
    ('PRO', 'Professional'),
    ('ELI', 'Elite'),
    ('WOC', 'World Class'),
    ('LEG', 'Legendary'),
    ('GDL', 'Godlike'),
    ]

    # les differentes frequente de la pratique sportives allant de l'occasionnel amateur a l'intensif professionnel
    FREQUENCE_PRACTICE = [
    ('OCC', 'Occasional'),
    ('REG', 'Regular'),
    ('INT', 'Intensive'),
    ('PRO', 'Professional'),
    ('OTH', 'Other'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Height in meters", blank=True, null=True)
    weight = models.FloatField(help_text="Weight in kilograms", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="players/profile_pictures/", blank=True, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="players")  # Changed to ForeignKey
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="players", blank=True, null=True)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, blank=True, null=True)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, blank=True, null=True)
    frequence = models.CharField(max_length=3, choices=FREQUENCE_PRACTICE, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True, help_text="Player's notable achievements")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    niveau = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], help_text="Player's level from 0 to 10")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

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