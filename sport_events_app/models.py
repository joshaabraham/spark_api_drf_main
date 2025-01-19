from django.db import models

from Player.models import Player
from equipe_app.models import Team
from localisation_app.models import GeoCoordinates
from sport_app.models import Sport



class Sponsor(models.Model):
    name = models.CharField(max_length=255)  # Nom du sponsor
    industry = models.CharField(max_length=100)  # Secteur d'activité
    contribution_amount = models.DecimalField(max_digits=15, decimal_places=2)  # Montant de la contribution
    logo_url = models.URLField(blank=True, null=True)  # URL du logo

class MediaCoverage(models.Model):
    media_outlet = models.CharField(max_length=255)  # Nom du média
    coverage_type = models.CharField(max_length=100)  # Type de média
    coverage_details = models.TextField(blank=True, null=True)  # Détails sur la couverture
    coverage_date = models.DateTimeField()  # Date de couverture

class Location(models.Model):
    name = models.CharField(max_length=255)  # Nom du lieu
    address = models.TextField(blank=True, null=True)  # Adresse facultative
    coordinates = models.ForeignKey(GeoCoordinates, on_delete=models.CASCADE, related_name="location")  # Coordonnées géographiques

class Match(models.Model):
    match_date = models.DateTimeField()  # Date et heure du match
    venue = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="matches")  # Lieu du match
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_a")  # Première équipe
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_b")  # Deuxième équipe
    result = models.CharField(max_length=50, blank=True, null=True)  # Résultat du match
    key_players = models.ManyToManyField(Player, related_name="key_matches")  # Joueurs clés du match

class SportEvent(models.Model):
    name = models.CharField(max_length=255)  # Nom de l'événement
    location = models.CharField(max_length=255)  # Lieu principal
    coordinates = models.OneToOneField(GeoCoordinates, on_delete=models.SET_NULL, null=True, related_name="sport_events")  # Coordonnées géographiques
    start_date = models.DateTimeField()  # Date de début
    end_date = models.DateTimeField()  # Date de fin
    organizer = models.CharField(max_length=255)  # Organisateur
    sports = models.ManyToManyField(Sport, related_name="events")  # Sports inclus
    participating_teams = models.ManyToManyField(Team, related_name="events")  # Équipes participantes
    notable_players = models.ManyToManyField(Player, related_name="notable_events")  # Joueurs célèbres participants
    description = models.TextField(blank=True, null=True)  # Description détaillée
    estimated_audience = models.PositiveIntegerField()  # Nombre estimé de spectateurs
    is_recurring = models.BooleanField(default=False)  # Indique si l'événement est récurrent
    recurrence_interval_years = models.PositiveIntegerField(blank=True, null=True)  # Intervalle de récurrence (en années)
    matches = models.ManyToManyField(Match, related_name="sport_events")  # Matchs inclus
    sponsors = models.ManyToManyField(Sponsor, related_name="sponsored_events")  # Sponsors
    media_coverage_details = models.ManyToManyField(MediaCoverage, related_name="covered_events")  # Couverture médiatique
