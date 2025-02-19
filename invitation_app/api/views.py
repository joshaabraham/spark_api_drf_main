from rest_framework import generics
from invitation_app.models import Invitation, InvitationNote, ProposedDate
from .serializers import InvitationNoteSerializer, InvitationSerializer, ProposedDateSerializer

class ProposedDateListCreateView(generics.ListCreateAPIView):
    queryset = ProposedDate.objects.all()
    serializer_class = ProposedDateSerializer

class ProposedDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProposedDate.objects.all()
    serializer_class = ProposedDateSerializer

class InvitationListCreateView(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class InvitationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class InvitationNoteListCreateView(generics.ListCreateAPIView):
    queryset = InvitationNote.objects.all()
    serializer_class = InvitationNoteSerializer

class InvitationNoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvitationNote.objects.all()
    serializer_class = InvitationNoteSerializer