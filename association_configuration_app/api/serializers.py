from rest_framework import serializers
from association_configuration_app.models import SportsAssociationConfiguration

class SportsAssociationConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsAssociationConfiguration
        fields = '__all__'