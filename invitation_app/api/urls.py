from django.urls import path
from .views import InvitationDetailView, InvitationListCreateView, InvitationNoteDetailView, InvitationNoteListCreateView, ProposedDateDetailView, ProposedDateListCreateView

urlpatterns = [
    path('proposed-dates/', ProposedDateListCreateView.as_view(), name='proposed-date-list-create'),
    path('proposed-dates/<int:pk>/', ProposedDateDetailView.as_view(), name='proposed-date-detail'),
    path('invitations/', InvitationListCreateView.as_view(), name='invitation-list-create'),
    path('invitations/<int:pk>/', InvitationDetailView.as_view(), name='invitation-detail'),
    path('invitation-notes/', InvitationNoteListCreateView.as_view(), name='invitation-note-list-create'),
    path('invitation-notes/<int:pk>/', InvitationNoteDetailView.as_view(), name='invitation-note-detail'),
]