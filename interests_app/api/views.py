from rest_framework import generics
from interests_app.models import UserInterest
from .serializers import UserInterestSerializer

class UserInterestListCreateView(generics.ListCreateAPIView):
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer

class UserInterestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer