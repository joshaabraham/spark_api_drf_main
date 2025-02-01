from rest_framework import serializers
from publicite_app.models import (
    Calendrier, PubliciteBase, PubliciteVideo, PubliciteBanniere, PubliciteCarrousel, PubliciteNative, Media, CtaButton,CampagnePublicitaire, BudgetCampagne,
    PageFacebook, ControleAudience
)

class ControleAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAudience
        fields = '__all__'

class CalendrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendrier
        fields = '__all__'

class CampagnePublicitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampagnePublicitaire
        fields = '__all__'
        
class PageFacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageFacebook
        fields = '__all__'
        
class BudgetCampagneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCampagne
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CtaButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtaButton
        fields = '__all__'

class PubliciteBaseSerializer(serializers.ModelSerializer):
    media = MediaSerializer()
    cta_button = CtaButtonSerializer()

    class Meta:
        model = PubliciteBase
        fields = '__all__'

class PubliciteVideoSerializer(PubliciteBaseSerializer):
    class Meta:
        model = PubliciteVideo
        fields = '__all__'

class PubliciteBanniereSerializer(PubliciteBaseSerializer):
    class Meta:
        model = PubliciteBanniere
        fields = '__all__'

class PubliciteCarrouselSerializer(PubliciteBaseSerializer):
    class Meta:
        model = PubliciteCarrousel
        fields = '__all__'

class PubliciteNativeSerializer(PubliciteBaseSerializer):
    class Meta:
        model = PubliciteNative
        fields = '__all__'
