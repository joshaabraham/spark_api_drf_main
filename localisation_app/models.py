from django.db import models
from django.conf import settings
from geopy.geocoders import Nominatim

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}")
        
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude

        super().save(*args, **kwargs)