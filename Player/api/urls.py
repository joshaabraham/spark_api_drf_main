from django.urls import path
from .views import PlayerListCreateView, PlayerRetrieveUpdateDestroyView

urlpatterns = [
    path('players/', PlayerListCreateView.as_view(), name='player-list-create'),
    path('players/<int:pk>/', PlayerRetrieveUpdateDestroyView.as_view(), name='player-detail'),
]