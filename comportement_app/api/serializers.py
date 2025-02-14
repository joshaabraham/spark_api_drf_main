from rest_framework import serializers
from comportement_app.models import UserComportement

class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComportement
        fields = '__all__'