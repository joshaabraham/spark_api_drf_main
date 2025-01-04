from rest_framework import generics
from sport_events_app.models import (
    GeoCoordinates, Sport, Player, Team, Sponsor,
    MediaCoverage, Location, Match, SportEvent
)
from .serializers import (
    GeoCoordinatesSerializer, SportSerializer, PlayerSerializer,
    TeamSerializer, SponsorSerializer, MediaCoverageSerializer,
    LocationSerializer, MatchSerializer, SportEventSerializer
)

class GeoCoordinatesListCreateView(generics.ListCreateAPIView):
    queryset = GeoCoordinates.objects.all()
    serializer_class = GeoCoordinatesSerializer

class GeoCoordinatesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeoCoordinates.objects.all()
    serializer_class = GeoCoordinatesSerializer

class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class MediaCoverageListCreateView(generics.ListCreateAPIView):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer

class MediaCoverageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MatchListCreateView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class SportEventListCreateView(generics.ListCreateAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer

class SportEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer
