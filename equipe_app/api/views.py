from rest_framework import generics
from equipe_app.models import Team
from equipe_app.api.serializers import TeamSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# class PlayerListCreateView(generics.ListCreateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer

# class PlayerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer