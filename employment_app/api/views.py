from rest_framework import generics
from employment_app.models import JobApplication, JobOpportunity, RequiredLanguage, RequiredSkill
from employment_app.api.serializers import JobApplicationSerializer, JobOpportunitySerializer,  RequiredLanguageSerializer, RequiredSkillSerializer

class JobOpportunityListCreateView(generics.ListCreateAPIView):
    queryset = JobOpportunity.objects.all()
    serializer_class = JobOpportunitySerializer

class JobOpportunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOpportunity.objects.all()
    serializer_class = JobOpportunitySerializer

class RequiredSkillListCreateView(generics.ListCreateAPIView):
    queryset = RequiredSkill.objects.all()
    serializer_class = RequiredSkillSerializer

class RequiredSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequiredSkill.objects.all()
    serializer_class = RequiredSkillSerializer

class RequiredLanguageListCreateView(generics.ListCreateAPIView):
    queryset = RequiredLanguage.objects.all()
    serializer_class = RequiredLanguageSerializer

class RequiredLanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequiredLanguage.objects.all()
    serializer_class = RequiredLanguageSerializer

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer