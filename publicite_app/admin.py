from django.contrib import admin
from .models import (
    CampagnePublicitaire, PubliciteBase, PubliciteVideo, PubliciteBanniere, 
    PubliciteCarrousel, PubliciteNative, Media, CtaButton,
    ControleAudience, BudgetEtCalendrier, PageFacebook, BudgetCampagne
)

# Configuration d'affichage pour Media
class MediaAdmin(admin.ModelAdmin):
    list_display = ('url', 'type_media', 'duree', 'dimensions')
    search_fields = ('url', 'type_media')

# Configuration d'affichage pour CtaButton
class CtaButtonAdmin(admin.ModelAdmin):
    list_display = ('texte', 'lien', 'couleur')
    search_fields = ('texte', 'lien')

# Configuration d'affichage pour CampagnePublicitaire
class CampagnePublicitaireAdmin(admin.ModelAdmin):
    list_display = ('nom_campagne', 'type_achat', 'objectif', 'limite_depense', 'date_creation')
    search_fields = ('nom_campagne', 'type_achat', 'objectif')
    list_filter = ('type_achat', 'objectif', 'date_creation')
    ordering = ('-date_creation',)

# Configuration commune d'affichage pour les publicités
class PubliciteBaseAdmin(admin.ModelAdmin):
    list_display = ('nom_publicite', 'type_publicite', 'campagne_publicitaire', 'statut', 'date_creation')
    search_fields = ('nom_publicite', 'type_publicite', 'campagne_publicitaire__nom_campagne')
    list_filter = ('type_publicite', 'statut', 'campagne_publicitaire')
    ordering = ('-date_creation',)

# Configuration d'affichage pour PubliciteVideo
class PubliciteVideoAdmin(PubliciteBaseAdmin):
    list_display = ('nom_publicite', 'type_publicite', 'campagne_publicitaire', 'video_autoplay', 'video_muted', 'statut', 'date_creation')
    search_fields = PubliciteBaseAdmin.search_fields + ('video_autoplay',)
    list_filter = PubliciteBaseAdmin.list_filter + ('video_autoplay', 'video_muted')

# Configuration d'affichage pour PubliciteBanniere
class PubliciteBanniereAdmin(PubliciteBaseAdmin):
    list_display = ('nom_publicite', 'type_publicite', 'campagne_publicitaire', 'emplacement_banniere', 'dimensions', 'statut', 'date_creation')
    search_fields = PubliciteBaseAdmin.search_fields + ('emplacement_banniere',)
    list_filter = PubliciteBaseAdmin.list_filter + ('emplacement_banniere',)

# Configuration d'affichage pour PubliciteCarrousel
class PubliciteCarrouselAdmin(PubliciteBaseAdmin):
    list_display = ('nom_publicite', 'type_publicite', 'campagne_publicitaire', 'statut', 'date_creation')
    search_fields = PubliciteBaseAdmin.search_fields
    list_filter = PubliciteBaseAdmin.list_filter

# Configuration d'affichage pour PubliciteNative
class PubliciteNativeAdmin(PubliciteBaseAdmin):
    list_display = ('nom_publicite', 'type_publicite', 'campagne_publicitaire', 'source', 'statut', 'date_creation')
    search_fields = PubliciteBaseAdmin.search_fields + ('source',)
    list_filter = PubliciteBaseAdmin.list_filter + ('source',)
    
class ControleAudienceAdmin(admin.ModelAdmin):
    list_display = ('lieu', 'age_minimum', 'langues')
    search_fields = ('lieu', 'langues')

class BudgetEtCalendrierAdmin(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'heure_debut', 'heure_fin')
    search_fields = ('date_debut', 'date_fin')

class PageFacebookAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lien', 'logo')
    search_fields = ('nom', 'lien')

class BudgetCampagneAdmin(admin.ModelAdmin):
    list_display = ('type_budget', 'montant')
    search_fields = ('type_budget',)
    
class ControleAudienceAdmin(admin.ModelAdmin):
    list_display = ('lieu', 'age_minimum', 'langues')
    search_fields = ('lieu', 'langues')

# Enregistrement des modèles dans l'administration

admin.site.register(ControleAudience)
admin.site.register(BudgetEtCalendrier)
admin.site.register(PageFacebook)
admin.site.register(BudgetCampagne)
admin.site.register(CampagnePublicitaire, CampagnePublicitaireAdmin)
admin.site.register(PubliciteBase, PubliciteBaseAdmin)  # Enregistrement de la publicité de base pour d'autres types génériques
admin.site.register(PubliciteVideo, PubliciteVideoAdmin)
admin.site.register(PubliciteBanniere, PubliciteBanniereAdmin)
admin.site.register(PubliciteCarrousel, PubliciteCarrouselAdmin)
admin.site.register(PubliciteNative, PubliciteNativeAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(CtaButton, CtaButtonAdmin)
