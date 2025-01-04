from django.urls import path
from . import views

urlpatterns = [
    path("chatsCreateList/", views.ChatListCreateView.as_view(), name="chat_list_create"),
    path("chat/<int:pk>/", views.ChatRetrieveUpdateDestroyView.as_view(), name="chat_detail"),
    path("messagesCreateList/", views.MessageListCreateView.as_view(), name="message_create"),
    
]