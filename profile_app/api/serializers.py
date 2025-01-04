# serializers.py
from rest_framework import serializers
from profile_app.models import ProfileUser

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ['user', 'bio', 'location', 'birth_date', 'profile_image', 'cover_image',
                  'website', 'is_private', 'posts_count', 'followers_count', 'following_count', 'friends_count', 'date_joined']

        # On rend ces champs en lecture seule pour empêcher la modification manuelle de certaines valeurs
        read_only_fields = ['user', 'posts_count', 'followers_count', 'following_count', 'friends_count', 'date_joined']
