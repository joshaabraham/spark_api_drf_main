from rest_framework import serializers

from equipe_app.models import FinancialRecord, Match, Sponsorship, Team, TeamHistory


class TeamHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamHistory
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    histories = TeamHistorySerializer(many=True, read_only=True)
    players = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(source='home_team.name', read_only=True)
    away_team_name = serializers.CharField(source='away_team.name', read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class SponsorshipSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Sponsorship
        fields = '__all__'


class FinancialRecordSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = FinancialRecord
        fields = '__all__'
