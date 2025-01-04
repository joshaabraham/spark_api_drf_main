from rest_framework import generics
from sport_app.models import Sport
from .serializers import SportSerializer

class SportListCreateView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    
class SportRetrieveList(generics.ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer