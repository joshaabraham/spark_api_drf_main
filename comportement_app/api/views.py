from rest_framework import generics
from comportement_app.models import UserComportement
from comportement_app.api.serializers import UserActionSerializer

class UserComportementListCreateView(generics.ListCreateAPIView):
    queryset = UserComportement.objects.all()
    serializer_class = UserActionSerializer

class UserComportementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserComportement.objects.all()
    serializer_class = UserActionSerializer