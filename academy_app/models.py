from django.db import models
from django.conf import settings

from sport_app.models import Sport

class School(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="school",  default=None)
    sportFK = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='shool', default=1)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class Course(models.Model):
    title = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(default='', max_length=255)
    # sport
    # category = 
    # duration =
    # totalSection =
    # updatedAt =
    # featured = 
    # progress = 
    # isFree = models.BooleanField(default=True)
    # needToBeregister = models.BooleanField(default=False)
    # otherInformation


    def __str__(self):
        return self.name

class Section(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    subtitle = models.CharField(default='', max_length=255)
    content = models.TextField(blank=True, max_length=255)

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    subtitle = models.CharField(default='', max_length=255)
    content = models.TextField(blank=True, max_length=255)
    
    def __str__(self):
        return self.title


    def __str__(self):
        return self.title