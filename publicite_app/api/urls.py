from django.urls import path
from .views import (
    CalendrierDetailView, CalendrierListCreateView, CampagnePublicitaireListCreateView, CampagnePublicitaireDetailView,
    PubliciteListCreateView, PubliciteDetailView,
    ControleAudienceListCreateView, ControleAudienceDetailView,
    PageFacebookListCreateView, PageFacebookDetailView,
    BudgetCampagneListCreateView, BudgetCampagneDetailView
)

urlpatterns = [
    # URLs pour Campagnes Publicitaires
    path('campagnes/', CampagnePublicitaireListCreateView.as_view(), name='campagne-list-create'),
    path('campagnes/<int:pk>/', CampagnePublicitaireDetailView.as_view(), name='campagne-detail'),

    # URLs pour Publicités
    path('publicites/', PubliciteListCreateView.as_view(), name='publicite-list-create'),
    path('publicites/<int:pk>/', PubliciteDetailView.as_view(), name='publicite-detail'),
    
     # URLs for ControleAudience
    path('controle-audience/', ControleAudienceListCreateView.as_view(), name='controle-audience-list-create'),
    path('controle-audience/<int:pk>/', ControleAudienceDetailView.as_view(), name='controle-audience-detail'),

    # URLs for BudgetEtCalendrier
    path('budget-et-calendrier/', CalendrierListCreateView.as_view(), name='budget-et-calendrier-list-create'),
    path('budget-et-calendrier/<int:pk>/', CalendrierDetailView.as_view(), name='budget-et-calendrier-detail'),

    # URLs for PageFacebook
    path('page-facebook/', PageFacebookListCreateView.as_view(), name='page-facebook-list-create'),
    path('page-facebook/<int:pk>/', PageFacebookDetailView.as_view(), name='page-facebook-detail'),

    # URLs for BudgetCampagne
    path('budget-campagne/', BudgetCampagneListCreateView.as_view(), name='budget-campagne-list-create'),
    path('budget-campagne/<int:pk>/', BudgetCampagneDetailView.as_view(), name='budget-campagne-detail'),
    

]
