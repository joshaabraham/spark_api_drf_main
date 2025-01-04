from django.contrib import admin

from abonnement_app.models import Subscription, Payment

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Payment)

