from django.contrib import admin
from .models import Invitation, InvitationNote, ProposedDate

admin.site.register(Invitation)
admin.site.register(ProposedDate)
admin.site.register(InvitationNote)
