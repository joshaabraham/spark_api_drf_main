from rest_framework import serializers
from user_config.models import UserConfiguration

class UserConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = '__all__'