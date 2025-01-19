from rest_framework import generics
from localisation_app.models import Address
from localisation_app.api.serializers import AddressSerializer


import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GeocodeView(APIView):
    def get(self, request, *args, **kwargs):
        address = request.query_params.get('address')
        if not address:
            return Response({"error": "Address is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Requête vers l'API Google Geocoding
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": address, "key": settings.GOOGLE_MAPS_API_KEY}
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] != 'OK':
            return Response({"error": data.get('error_message', 'Unable to geocode address')}, status=status.HTTP_400_BAD_REQUEST)
        
        # Récupération des coordonnées
        coordinates = data['results'][0]['geometry']['location']
        return Response({"coordinates": coordinates})

class ReverseGeocodeView(APIView):
    def get(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        
        if not lat or not lng:
            return Response({"error": "Latitude and Longitude are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Requête vers l'API Google Geocoding
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"latlng": f"{lat},{lng}", "key": settings.GOOGLE_MAPS_API_KEY}
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] != 'OK':
            return Response({"error": data.get('error_message', 'Unable to reverse geocode coordinates')}, status=status.HTTP_400_BAD_REQUEST)
        
        # Récupération de l'adresse
        address = data['results'][0]['formatted_address']
        return Response({"address": address})



class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

