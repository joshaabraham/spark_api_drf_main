from datetime import timezone
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Choices pour l'état du produit
    ETAT_CHOICES = [
        ('neuf', 'Neuf'),
        ('comme_neuf', 'Comme neuf'),
        ('bon_etat', 'Bon état'),
        ('acceptable', 'Acceptable'),
        ('occasion', 'Occasion'),
    ]
    
    # Identité du produit
    nom = models.CharField(max_length=255, default='Nouveau produit')
    description = models.TextField()
    description_courte = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    est_neuf = models.BooleanField(default=True)
    
    # Catégorisation
    categorie = models.CharField(max_length=100, default='Autres')
    sous_categorie = models.CharField(max_length=100, blank=True, null=True)
    marque = models.CharField(max_length=100, blank=True, null=True)
    modele = models.CharField(max_length=100, blank=True, null=True)
    
    # Dates importantes
    date_mise_en_ligne = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    derniere_modification = models.DateTimeField(auto_now=True)
    
    # État
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='neuf')
    
    # Vendeur
    vendeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='produits', default=1)
    nom_vendeur = models.CharField(max_length=255, default='Anonyme')
    
    # Images
    images = models.JSONField(default=list, blank=True)  # Liste d'URLs ou de chemins
    
    # Localisation
    localisation = models.CharField(max_length=255, blank=True, null=True)
    pays_origine = models.CharField(max_length=100, blank=True, null=True)
    
    # Stock et vues
    stock = models.PositiveIntegerField(default=0)
    nombre_de_vues = models.PositiveIntegerField(default=0)
    
    # Livraison
    livraison_disponible = models.BooleanField(default=False)
    frais_de_livraison = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    methode_livraison = models.CharField(max_length=100, blank=True, null=True)
    
    # Taxe
    tva_incluse = models.BooleanField(default=True)
    taux_tva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    # Avis
    note_moyenne = models.FloatField(default=0.0)
    nombre_avis = models.PositiveIntegerField(default=0)
    
    # SEO et mots-clés
    mots_cles = models.JSONField(default=list, blank=True)  # Liste de mots-clés
    meta_titre = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_mots_cles = models.JSONField(default=list, blank=True)  # Liste pour SEO
    
    # Promotions
    est_en_promotion = models.BooleanField(default=False)
    prix_avant_promotion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_debut_promotion = models.DateTimeField(blank=True, null=True)
    date_fin_promotion = models.DateTimeField(blank=True, null=True)
    
    # Enchères
    est_en_enchere = models.BooleanField(default=False)
    prix_depart_enchere = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_debut_enchere = models.DateTimeField(blank=True, null=True)
    date_fin_enchere = models.DateTimeField(blank=True, null=True)
    meilleur_encherisseur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='enchere_produits')
    prix_actuel_enchere = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Autres attributs
    statut = models.CharField(max_length=50, default='Publié')
    nombre_vendus = models.PositiveIntegerField(default=0)
    est_mis_en_avant = models.BooleanField(default=False)
    duree_retour = models.PositiveIntegerField(blank=True, null=True)  # En jours
    politique_retour = models.TextField(blank=True, null=True)
    
    def obtenir_prix_final(self):
        """Calcule le prix final après application de la promotion."""
        if self.est_en_promotion and self.date_debut_promotion and self.date_fin_promotion:
            maintenant = timezone.now()
            if self.date_debut_promotion <= maintenant <= self.date_fin_promotion:
                return self.prix
        return self.prix_avant_promotion or self.prix

    def __str__(self):
        return self.nom


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.pk} - {self.customer.user.username}"

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
