import geocoder
import os
from geopy.geocoders import GoogleV3
from dotenv import load_dotenv


load_dotenv()

def get_geocode(address):
    google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    geolocator = GoogleV3(api_key=google_maps_api_key)
    
    try:
        location = geolocator.geocode(address)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude}
        else:
            return None
    except Exception as e:
        print(f"Error while getting geocode: {e}")
        return None

def get_coordinates_from_ip(ip_address):
    g = geocoder.ip(ip_address)

    if g.ok:
        return g.latlng
    else:
        return None

ip_address = "8.8.8.8"  # Remplacez cette valeur par l'adresse IP souhaitée
coordinates = get_coordinates_from_ip(ip_address)

if coordinates:
    print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
else:
    print("Impossible d'obtenir les coordonnées géographiques.")