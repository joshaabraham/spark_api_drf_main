from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import Player
from .serializers import PlayerSerializer

class PlayerPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class PlayerFilterView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['niveau', 'sport', 'frequence', 'gender']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    pagination_class = PlayerPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        age = self.request.query_params.get('age')
        if age is not None:
            age = int(age)
            from datetime import date, timedelta
            today = date.today()
            min_date_of_birth = today - timedelta(days=(age + 1) * 365)
            max_date_of_birth = today - timedelta(days=age * 365)
            queryset = queryset.filter(date_of_birth__range=(min_date_of_birth, max_date_of_birth))
        return queryset
