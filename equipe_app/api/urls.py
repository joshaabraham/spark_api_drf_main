from django.urls import path
from . import views

urlpatterns = [
    path('sports/', views.SportListCreateView.as_view(), name='sport-list-create'),
    path('sports/<int:pk>/', views.SportDetailView.as_view(), name='sport-detail'),
    path('teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
]