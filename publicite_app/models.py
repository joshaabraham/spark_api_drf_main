from django.db import models
from django.conf import settings


class BudgetCampagne(models.Model):
    TYPE_BUDGET_CHOICES = [
        ('quotidien', 'Quotidien'),
        ('global', 'Global')
    ]
    type_budget = models.CharField(max_length=50, choices=TYPE_BUDGET_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

class PageFacebook(models.Model):
    nom = models.CharField(max_length=255)
    lien = models.URLField(max_length=500)
    logo = models.URLField(max_length=500)

class Calendrier(models.Model):
    date_debut = models.DateField()
    heure_debut = models.TimeField()
    date_fin = models.DateField()
    heure_fin = models.TimeField()

class ControleAudience(models.Model):
    lieu = models.CharField(max_length=255)
    age_minimum = models.IntegerField()
    age_maximum = models.IntegerField()
    langues = models.JSONField()  # Liste de langues
    centre_interet = models.JSONField(blank=True, null=True)  # Liste de centres d'intérêt
    genre = models.CharField(max_length=10, blank=True, null=True)  # homme, femme, tous

class CampagnePublicitaire(models.Model):
    nom_campagne = models.CharField(max_length=255)
    type_achat = models.CharField(max_length=50)  # Enchères, Achat Direct, etc.
    objectif = models.CharField(max_length=100)  # Notoriété, Conversion, etc.
    categories_speciales_a_ecarter = models.JSONField()  # Liste de catégories exclues
    limite_depense = models.DecimalField(max_digits=10, decimal_places=2)
    budget_campagne = models.OneToOneField(BudgetCampagne, on_delete=models.CASCADE)
    page_facebook = models.OneToOneField(PageFacebook, on_delete=models.CASCADE)
    calendrier = models.OneToOneField(Calendrier, on_delete=models.CASCADE)
    controle_audience = models.OneToOneField(ControleAudience, on_delete=models.CASCADE)
    placement = models.CharField(max_length=255)
    liste_publicite = models.JSONField()  # Liste de publicités associées
    statut_campagne = models.CharField(max_length=50, blank=True, null=True)  # En cours, Terminée, etc.
    taux_clics = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nombre_impressions = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur_responsable = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ad_campaigns")


# definition d une publicite


class Media(models.Model):
    TYPE_MEDIA_CHOICES = [
        ('image', 'Image'),
        ('video', 'Vidéo'),
        ('gif', 'GIF'),
    ]
    url = models.URLField(max_length=500)
    type_media = models.CharField(max_length=50, choices=TYPE_MEDIA_CHOICES)
    duree = models.IntegerField(blank=True, null=True)  # Durée en secondes pour les vidéos
    dimensions = models.CharField(max_length=50, blank=True, null=True)  # Dimensions en pixels

class CtaButton(models.Model):
    texte = models.CharField(max_length=255)
    lien = models.URLField(max_length=500)
    couleur = models.CharField(max_length=20)  # Code couleur hexadécimal

class PubliciteBase(models.Model):
    TYPE_PUBLICITE_CHOICES = [
        ('video', 'Vidéo'),
        ('banniere', 'Bannière'),
        ('carrousel', 'Carrousel'),
        ('native', 'Native'),
    ]
    campagne_publicitaire = models.ForeignKey(
        CampagnePublicitaire, 
        on_delete=models.CASCADE, 
        related_name='publicites'
    )  # Relation vers la campagne publicitaire
    ordreAffichage = models.IntegerField(blank=True, null=True)
    type_publicite = models.CharField(max_length=50, choices=TYPE_PUBLICITE_CHOICES)
    nom_publicite = models.CharField(max_length=255)
    texte_principal = models.TextField()
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    url_destination = models.URLField(max_length=500, blank=True, null=True)
    cta_button = models.OneToOneField(CtaButton, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, blank=True, null=True)  # Actif, Inactif, En attente
    impressions = models.IntegerField(blank=True, null=True)
    clics = models.IntegerField(blank=True, null=True)
    taux_conversion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class PubliciteVideo(PubliciteBase):
    video_autoplay = models.BooleanField(default=True)
    video_muted = models.BooleanField(default=False)

class PubliciteBanniere(PubliciteBase):
    emplacement_banniere = models.CharField(max_length=255)  # Header, Sidebar, etc.
    dimensions = models.CharField(max_length=50)  # Dimensions spécifiques

class PubliciteCarrousel(PubliciteBase):
    liste_images = models.ManyToManyField(Media)  # Liste des images/vidéos du carrousel

class PubliciteNative(PubliciteBase):
    source = models.CharField(max_length=255)  # Recommandé par, sponsorisé par, etc.


# Filtre pour CampagnePublicitaire
class CampagnePublicitaireFilter(filters.FilterSet):
    nom_campagne = filters.CharFilter(lookup_expr='icontains')
    type_achat = filters.CharFilter(lookup_expr='iexact')
    objectif = filters.CharFilter(lookup_expr='iexact')
    limite_depense = filters.RangeFilter()
    statut_campagne = filters.CharFilter(lookup_expr='iexact')
    taux_clics = filters.RangeFilter()
    nombre_impressions = filters.RangeFilter()
    date_creation = filters.DateFromToRangeFilter()
    owner = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = CampagnePublicitaire
        fields = ['nom_campagne', 'type_achat', 'objectif', 'limite_depense', 'statut_campagne', 'taux_clics', 'nombre_impressions', 'date_creation', 'owner']
