from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from chat_app.models import Chat, Message, GroupInvitation, MessageStatus
from .serializers import ChatSerializer, MessageSerializer, GroupInvitationSerializer, MessageStatusSerializer


# Chats
class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# Messages
class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat_id=chat_id)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Group Invitations
class GroupInvitationListCreateView(generics.ListCreateAPIView):
    queryset = GroupInvitation.objects.all()
    serializer_class = GroupInvitationSerializer


class GroupInvitationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupInvitation.objects.all()
    serializer_class = GroupInvitationSerializer


# Mark a message as read
class MarkMessageAsReadView(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            message = Message.objects.get(pk=pk)
            MessageStatus.objects.update_or_create(
                message=message,
                user=request.user,
                defaults={'is_read': True, 'read_at': timezone.now()}
            )
            return Response({"message": "Message marked as read"}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)