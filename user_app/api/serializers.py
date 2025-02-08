from profile_app.models import ProfileUser
from comportement_app.models import UserComportement
from user_config.models import UserConfiguration
from user_app.models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        CustomUser = get_user_model()
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            "email": {"write_only": True},
            "friends": {"required": False},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance, validated_data)
    
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ['bio', 'location', 'birth_date', 'profile_image', 'cover_image']

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = ['setting1', 'setting2']  # Remplacez par les champs réels de votre modèle de configuration
        
class ComportementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComportement
        fields = ['behavior1', 'behavior2']  # Remplacez par les champs réels de votre modèle de comportement