import code
from django.db import models

# Create your models here.

class Sport(models.Model):
        code = models.CharField(max_length=4)
        categorie = models.CharField(max_length=150, default=None)
        
        sp_titre_fr = models.CharField(max_length=150, default=None)
        sp_titre_en = models.CharField(max_length=150, default=None)
        sp_titre_por = models.CharField(max_length=150, default=None)
        sp_titre_ko = models.CharField(max_length=150, default=None)
        sp_titre_jp = models.CharField(max_length=150, default=None)
        sp_titre_es = models.CharField(max_length=150, default=None)
        sp_titre_ru = models.CharField(max_length=150, default=None)
        sp_titre_ind = models.CharField(max_length=150, default=None)
        sp_titre_pol = models.CharField(max_length=150, default=None)
        sp_titre_ita = models.CharField(max_length=150, default=None)
        
        
        icon_petit = models.ImageField(max_length=150)
        icon_grand = models.ImageField(max_length=150)

        dateCreation = models.DateTimeField(auto_now_add=True, null=False)
        dateMiseAJour = models.DateTimeField(auto_now=True, null=False)

        def __str__(self):
                return self.sp_titre_fr