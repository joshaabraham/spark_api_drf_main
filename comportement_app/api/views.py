from rest_framework import generics
from comportement_app.models import UserAction
from comportement_app.api.serializers import UserActionSerializer

class UserActionListCreateView(generics.ListCreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

class UserActionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer