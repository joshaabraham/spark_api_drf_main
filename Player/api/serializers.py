from rest_framework import serializers
from models import  Player
from equipe_app.api.serializers import TeamSerializer
from sport_app.api.serializers import SportSerializer

class PlayerSerializer(serializers.ModelSerializer):
    sports = SportSerializer(many=True, read_only=True)
    team = TeamSerializer(read_only=True)
    bmi = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'

    def get_bmi(self, obj):
        return obj.bmi()

    def get_age(self, obj):
        return obj.age()