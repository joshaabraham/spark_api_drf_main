from django.urls import path
from .views import (
    ChatListCreateView, ChatRetrieveUpdateDestroyView,
    MessageListCreateView, MessageRetrieveUpdateDestroyView,
    GroupInvitationListCreateView, GroupInvitationRetrieveUpdateDestroyView,
    MarkMessageAsReadView
)

urlpatterns = [
    # Chats
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chats/<int:pk>/', ChatRetrieveUpdateDestroyView.as_view(), name='chat-detail'),

    # Messages
    path('chats/<int:chat_id>/messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-detail'),

    # Group Invitations
    path('group-invitations/', GroupInvitationListCreateView.as_view(), name='group-invitation-list-create'),
    path('group-invitations/<int:pk>/', GroupInvitationRetrieveUpdateDestroyView.as_view(), name='group-invitation-detail'),

    # Mark message as read
    path('messages/<int:pk>/mark-as-read/', MarkMessageAsReadView.as_view(), name='mark-message-as-read'),
]