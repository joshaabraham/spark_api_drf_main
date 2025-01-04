from rest_framework import serializers
from sport_app.models import Sport



class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'