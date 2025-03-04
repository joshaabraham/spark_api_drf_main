from rest_framework import filters
from django.db.models import Q
from math import radians, cos, sin, asin, sqrt

class NearbyFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        lat = request.query_params.get('latitude')
        lon = request.query_params.get('longitude')
        radius = request.query_params.get('radius', 10)  # Default radius is 10 km

        if lat is None or lon is None:
            return queryset

        lat = float(lat)
        lon = float(lon)
        radius = float(radius)

        def haversine(lat1, lon1, lat2, lon2):
            # Convert decimal degrees to radians
            lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
            # Haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            r = 6371  # Radius of earth in kilometers
            return c * r

        nearby_invitations = [
            invitation.pk for invitation in queryset
            if haversine(lat, lon, invitation.latitude, invitation.longitude) <= radius
        ]

        return queryset.filter(pk__in=nearby_invitations)