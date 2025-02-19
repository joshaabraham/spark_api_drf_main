from rest_framework import serializers
from invitation_app.models import Invitation, InvitationNote, ProposedDate

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        # fields = ['id', 'sender', 'receiver', 'date', 'location', 'created_at', 'updated_at']
        fields = '__all__'
        
class ProposedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposedDate
        # fields = ['id', 'sender', 'receiver', 'date', 'location', 'created_at', 'updated_at']
        fields = '__all__'
        
class InvitationNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationNote
        # fields = ['id', 'sender', 'receiver', 'date', 'location', 'created_at', 'updated_at']
        fields = '__all__'
        
        
# class InvitationStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InvitationStatus
#         # fields = ['id', 'sender', 'receiver', 'date', 'location', 'created_at', 'updated_at']
#         fields = '__all__'