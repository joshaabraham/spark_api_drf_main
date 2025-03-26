from rest_framework import serializers
from chat_app.models import Chat, Message, GroupInvitation, MessageStatus

class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Chat
        fields = ['id', 'chat_type', 'name', 'participants', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'timestamp', 'is_read']

class GroupInvitationSerializer(serializers.ModelSerializer):
    invited_user = serializers.StringRelatedField()
    invited_by = serializers.StringRelatedField()

    class Meta:
        model = GroupInvitation
        fields = ['id', 'chat', 'invited_user', 'invited_by', 'created_at', 'accepted']

class MessageStatusSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = MessageStatus
        fields = ['id', 'message', 'user', 'is_read', 'read_at']