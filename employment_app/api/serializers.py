from rest_framework import serializers
from employment_app.models import JobOpportunity, RequiredSkill, RequiredLanguage, JobApplication

class JobOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpportunity
        fields = '__all__'

class RequiredSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredSkill
        fields = '__all__'

class RequiredLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredLanguage
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'