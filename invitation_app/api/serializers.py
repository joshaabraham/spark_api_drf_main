from rest_framework import serializers
from invitation_app.models import Invitation

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        # fields = ['id', 'sender', 'receiver', 'date', 'location', 'created_at', 'updated_at']
        fields = '__all__'