from rest_framework import serializers
from academy_app.models import School, Teacher, Student, Course, Section, Chapter
from user_app.api.serializers import UserSerializer
from sport_app.models import Sport
from sport_app.api.serializers import SportSerializer

class SchoolSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    sport = SportSerializer(read_only=True)  # Utilise un serializer imbriqué pour afficher les détails de la catégorie
    sport_id = serializers.PrimaryKeyRelatedField(queryset=Sport.objects.all(), source='sport', write_only=True)  # Permet d'envoyer l'ID de la catégorie dans les requêtes
    
    class Meta:
        model = School
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'