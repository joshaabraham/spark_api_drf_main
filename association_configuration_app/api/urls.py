from django.urls import path
from association_configuration_app.api.views import SportsAssociationConfigurationListCreateView, SportsAssociationConfigurationRetrieveUpdateDestroyView

urlpatterns = [
    path("sports_association_configurationsCreateList/", SportsAssociationConfigurationListCreateView.as_view(), name="sports_association_configuration_create"),
    path("sports_association_configuration/<int:pk>/", SportsAssociationConfigurationRetrieveUpdateDestroyView.as_view(), name="sports_association_configuration_detail"),
]