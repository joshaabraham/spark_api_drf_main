from django.urls import path
from . import views

urlpatterns = [
    path("user_configurations/", views.UserConfigurationListCreateView.as_view(), name="user_configuration_list_create"),
    path("user_configurations/<int:pk>/", views.UserConfigurationRetrieveUpdateDestroyView.as_view(), name="user_configuration_detail"),
]