from django.urls import path
from . import views

urlpatterns = [
    path("teamsCreateList/", views.TeamListCreateView.as_view(), name="team_list_create"),
    path("team/<int:pk>/", views.TeamRetrieveUpdateDestroyView.as_view(), name="team_detail"),
    # path("playersCreateList/", views.PlayerListCreateView.as_view(), name="player_list_create"),
    # path("player/<int:pk>/", views.PlayerRetrieveUpdateDestroyView.as_view(), name="player_detail"),
]