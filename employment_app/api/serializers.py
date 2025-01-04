from rest_framework import serializers
from employment_app.models import JobOffer, JobSearch

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'

class JobSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSearch
        fields = '__all__'