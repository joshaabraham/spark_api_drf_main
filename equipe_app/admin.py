from django.contrib import admin

from equipe_app.models import FinancialRecord, Match, Sponsorship, Team, TeamHistory

# Register your models here.
admin.site.register(Team)
admin.site.register(TeamHistory)
admin.site.register(Match)
admin.site.register(Sponsorship)
admin.site.register(FinancialRecord)
# admin.site.register(Player)
