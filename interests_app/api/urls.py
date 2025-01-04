from django.urls import path
from .views import UserInterestListCreateView, UserInterestRetrieveUpdateDestroyView

urlpatterns = [
    path('userinterests/', UserInterestListCreateView.as_view(), name='userinterests-list-create'),
    path('userinterests/<int:pk>/', UserInterestRetrieveUpdateDestroyView.as_view(), name='userinterests-retrieve-update-destroy'),
]