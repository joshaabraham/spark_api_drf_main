from rest_framework import serializers
from localisation_app.models import Address
from user_app.api.serializers import UserSerializer

class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'