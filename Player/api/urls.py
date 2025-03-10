from django.urls import path
from .views import PlayerFilterView

urlpatterns = [
    path('players/', PlayerFilterView.as_view(), name='player-filter'),
]