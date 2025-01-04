from rest_framework import generics
from rest_framework.response import Response
from publicite_app.models import CampagnePublicitaire, PubliciteBase, PubliciteVideo, PubliciteBanniere, PubliciteCarrousel, PubliciteNative, ControleAudience, BudgetEtCalendrier, PageFacebook, BudgetCampagne
from publicite_app.api.serializers import CampagnePublicitaireSerializer,  PubliciteBaseSerializer, PubliciteVideoSerializer, PubliciteBanniereSerializer, PubliciteCarrouselSerializer, PubliciteNativeSerializer,ControleAudienceSerializer, BudgetEtCalendrierSerializer, PageFacebookSerializer, BudgetCampagneSerializer

from rest_framework import generics

# Views for ControleAudience
class ControleAudienceListCreateView(generics.ListCreateAPIView):
    queryset = ControleAudience.objects.all()
    serializer_class = ControleAudienceSerializer

class ControleAudienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ControleAudience.objects.all()
    serializer_class = ControleAudienceSerializer

# Views for BudgetEtCalendrier
class BudgetEtCalendrierListCreateView(generics.ListCreateAPIView):
    queryset = BudgetEtCalendrier.objects.all()
    serializer_class = BudgetEtCalendrierSerializer

class BudgetEtCalendrierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BudgetEtCalendrier.objects.all()
    serializer_class = BudgetEtCalendrierSerializer

# Views for PageFacebook
class PageFacebookListCreateView(generics.ListCreateAPIView):
    queryset = PageFacebook.objects.all()
    serializer_class = PageFacebookSerializer

class PageFacebookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PageFacebook.objects.all()
    serializer_class = PageFacebookSerializer

# Views for BudgetCampagne
class BudgetCampagneListCreateView(generics.ListCreateAPIView):
    queryset = BudgetCampagne.objects.all()
    serializer_class = BudgetCampagneSerializer

class BudgetCampagneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BudgetCampagne.objects.all()
    serializer_class = BudgetCampagneSerializer

# ListCreateAPIView pour lister et créer des campagnes
class CampagnePublicitaireListCreateView(generics.ListCreateAPIView):
    queryset = CampagnePublicitaire.objects.all()
    serializer_class = CampagnePublicitaireSerializer

# RetrieveUpdateDestroyAPIView pour récupérer, mettre à jour et supprimer une campagne
class CampagnePublicitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CampagnePublicitaire.objects.all()
    serializer_class = CampagnePublicitaireSerializer

# ListCreateAPIView pour lister et créer des publicités
class PubliciteListCreateView(generics.ListCreateAPIView):
    queryset = PubliciteBase.objects.all()
    serializer_class = PubliciteBaseSerializer

    def get_serializer_class(self):
        # Sélection du bon serializer en fonction du type de publicité
        type_publicite = self.request.data.get('type_publicite')
        if type_publicite == 'video':
            return PubliciteVideoSerializer
        elif type_publicite == 'banniere':
            return PubliciteBanniereSerializer
        elif type_publicite == 'carrousel':
            return PubliciteCarrouselSerializer
        elif type_publicite == 'native':
            return PubliciteNativeSerializer
        return super().get_serializer_class()

# RetrieveUpdateDestroyAPIView pour récupérer, mettre à jour et supprimer une publicité
class PubliciteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PubliciteBase.objects.all()
    serializer_class = PubliciteBaseSerializer

    def get_serializer_class(self):
        # Sélection du bon serializer en fonction du type de publicité
        type_publicite = self.get_object().type_publicite
        if type_publicite == 'video':
            return PubliciteVideoSerializer
        elif type_publicite == 'banniere':
            return PubliciteBanniereSerializer
        elif type_publicite == 'carrousel':
            return PubliciteCarrouselSerializer
        elif type_publicite == 'native':
            return PubliciteNativeSerializer
        return super().get_serializer_class()