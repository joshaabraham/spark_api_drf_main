from rest_framework import generics
from association_configuration_app.models import SportsAssociationConfiguration
from association_configuration_app.api.serializers import SportsAssociationConfigurationSerializer

class SportsAssociationConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = SportsAssociationConfiguration.objects.all()
    serializer_class = SportsAssociationConfigurationSerializer

class SportsAssociationConfigurationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportsAssociationConfiguration.objects.all()
    serializer_class = SportsAssociationConfigurationSerializer