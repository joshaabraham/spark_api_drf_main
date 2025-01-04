from rest_framework import generics
from employment_app.models import JobOffer, JobSearch
from .serializers import JobOfferSerializer, JobSearchSerializer

class JobOfferListCreateView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer

class JobOfferRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer

class JobSearchListCreateView(generics.ListCreateAPIView):
    queryset = JobSearch.objects.all()
    serializer_class = JobSearchSerializer

class JobSearchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobSearch.objects.all()
    serializer_class = JobSearchSerializer