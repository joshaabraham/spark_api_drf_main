from django.contrib import admin

from academy_app.models import School, Teacher, Student, Course, Section, Chapter

# Register your models here.
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Chapter)
