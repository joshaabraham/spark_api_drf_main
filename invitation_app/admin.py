from django.contrib import admin
from invitation_app.models import Invitation
# Register your models here.
admin.site.register(Invitation)
admin.site.register(ProposedDate)
admin.site.register(InvitationNote)
admin.site.register(InvitationStatus)
