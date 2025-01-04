from django.contrib import admin

from association_app.models import Member, SportEvent, Promotion, Subscription

# Register your models here.
admin.site.register(Member)
admin.site.register(SportEvent)
admin.site.register(Promotion)
admin.site.register(Subscription)