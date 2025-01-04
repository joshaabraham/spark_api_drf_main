from rest_framework import serializers
from contact_app.models import Contact
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'