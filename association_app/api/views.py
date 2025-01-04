from rest_framework import generics
from association_app.models import Member, SportEvent, Promotion, Subscription
from .serializers import MemberSerializer, SportEventSerializer, PromotionSerializer, SubscriptionSerializer

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class SportEventListCreateView(generics.ListCreateAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer

class SportEventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer

class PromotionListCreateView(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer