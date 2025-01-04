from django.urls import path
from .views import SportListCreateView, SportRetrieveUpdateDestroyView, SportRetrieveList

urlpatterns = [
    path('sportCreate/', SportListCreateView.as_view(), name='sport_create'),
    path('sport/<int:pk>/', SportRetrieveUpdateDestroyView.as_view(), name='sport_retrieve_update_destroy'),
    path('sport/list/', SportRetrieveList.as_view(), name='sport_list'),
    
]