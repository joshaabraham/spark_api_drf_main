from django.urls import path
from .views import (
    GeoCoordinatesListCreateView, GeoCoordinatesDetailView,
    SportListCreateView, SportDetailView,
    PlayerListCreateView, PlayerDetailView,
    TeamListCreateView, TeamDetailView,
    SponsorListCreateView, SponsorDetailView,
    MediaCoverageListCreateView, MediaCoverageDetailView,
    LocationListCreateView, LocationDetailView,
    MatchListCreateView, MatchDetailView,
    SportEventListCreateView, SportEventDetailView
)

urlpatterns = [
    path('geo-coordinates/', GeoCoordinatesListCreateView.as_view(), name='geo-coordinates-list'),
    path('geo-coordinates/<int:pk>/', GeoCoordinatesDetailView.as_view(), name='geo-coordinates-detail'),
    path('sponsors/', SponsorListCreateView.as_view(), name='sponsors-list'),
    path('sponsors/<int:pk>/', SponsorDetailView.as_view(), name='sponsors-detail'),
    path('media-coverage/', MediaCoverageListCreateView.as_view(), name='media-coverage-list'),
    path('media-coverage/<int:pk>/', MediaCoverageDetailView.as_view(), name='media-coverage-detail'),
    path('locations/', LocationListCreateView.as_view(), name='locations-list'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='locations-detail'),
    path('matches/', MatchListCreateView.as_view(), name='matches-list'),
    path('matches/<int:pk>/', MatchDetailView.as_view(), name='matches-detail'),
    # path('sport-events/', SportEventListCreateView.as_view(), name='sport-events-list'),
    path('sport-events/', SportEventFilterView.as_view(), name='sport-event-filter'),
    path('sport-events/<int:pk>/', SportEventDetailView.as_view(), name='sport-events-detail'),
]
