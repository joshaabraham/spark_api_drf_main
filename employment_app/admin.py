from django.contrib import admin

from employment_app.models import JobOffer, JobSearch

# Register your models here.
admin.site.register(JobOffer)
admin.site.register(JobSearch)
