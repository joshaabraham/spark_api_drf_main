from rest_framework import generics
from user_config.models import UserConfiguration
from .serializers import UserConfigurationSerializer

class UserConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = UserConfiguration.objects.all()
    serializer_class = UserConfigurationSerializer

class UserConfigurationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserConfiguration.objects.all()
    serializer_class = UserConfigurationSerializer