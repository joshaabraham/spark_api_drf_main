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
