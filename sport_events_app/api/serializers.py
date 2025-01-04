from rest_framework import serializers
from Player.api.serializers import PlayerSerializer
from equipe_app.api.serializers import TeamSerializer
from sport_app.api.serializers import SportSerializer
from models import (
    GeoCoordinates, Sponsor,
    MediaCoverage, Location, Match, SportEvent
)

class GeoCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoCoordinates
        fields = ['id', 'latitude', 'longitude']

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'industry', 'contribution_amount', 'logo_url']

class MediaCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCoverage
        fields = ['id', 'media_outlet', 'coverage_type', 'coverage_details', 'coverage_date']

class LocationSerializer(serializers.ModelSerializer):
    coordinates = GeoCoordinatesSerializer()

    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'coordinates']

class MatchSerializer(serializers.ModelSerializer):
    venue = LocationSerializer()
    team_a = TeamSerializer()
    team_b = TeamSerializer()
    key_players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = ['id', 'match_date', 'venue', 'team_a', 'team_b', 'result', 'key_players']

class SportEventSerializer(serializers.ModelSerializer):
    coordinates = GeoCoordinatesSerializer()
    sports = SportSerializer(many=True, read_only=True)
    participating_teams = TeamSerializer(many=True, read_only=True)
    notable_players = PlayerSerializer(many=True, read_only=True)
    matches = MatchSerializer(many=True, read_only=True)
    sponsors = SponsorSerializer(many=True, read_only=True)
    media_coverage_details = MediaCoverageSerializer(many=True, read_only=True)

    class Meta:
        model = SportEvent
        fields = [
            'id', 'name', 'location', 'coordinates', 'start_date', 'end_date', 
            'organizer', 'sports', 'participating_teams', 'notable_players',
            'description', 'estimated_audience', 'is_recurring',
            'recurrence_interval_years', 'matches', 'sponsors', 'media_coverage_details'
        ]
