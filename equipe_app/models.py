from django.db import models

from sport_app.models import Sport



class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='teams')
    city = models.CharField(max_length=100)
    stadium_name = models.CharField(max_length=100, blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    coach_name = models.CharField(max_length=100, blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    team_logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    championships_won = models.PositiveIntegerField(default=0)
    website = models.URLField(blank=True, null=True)
    social_media = models.JSONField(default=dict, blank=True)  # Ex: {"twitter": "...", "instagram": "..."}
    budget = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # Budget annuel
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.city})"


class TeamHistory(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='histories')
    season = models.CharField(max_length=10)  # Format : "2023/2024"
    league_position = models.PositiveIntegerField(blank=True, null=True)
    total_matches = models.PositiveIntegerField(default=0)
    total_wins = models.PositiveIntegerField(default=0)
    total_draws = models.PositiveIntegerField(default=0)
    total_losses = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - Saison {self.season}"


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    score_home = models.PositiveIntegerField(blank=True, null=True)
    score_away = models.PositiveIntegerField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    events = models.JSONField(default=list, blank=True)  # Ex: [{"minute": 23, "type": "goal", "player": "John Doe"}]

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.date.strftime('%Y-%m-%d %H:%M')}"


class Sponsorship(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='sponsorships')
    sponsor_name = models.CharField(max_length=100)
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sponsor_name} - {self.team.name}"


class FinancialRecord(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='financial_records')
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # Positive for income, negative for expenses
    is_income = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.team.name} - {self.description} ({self.amount})"
