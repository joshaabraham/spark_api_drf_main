from django.urls import path
from . import views

urlpatterns = [
    path("schoolCreateList/", views.SchoolListCreateView.as_view(), name="school_create"),
    path("school/<int:pk>/", views.SchoolRetrieveUpdateDestroyView.as_view(), name="school_detail"),

    path("teacherCreateList/", views.TeacherListCreateView.as_view(), name="teacher_create"),
    path("teacher/<int:pk>/", views.TeacherRetrieveUpdateDestroyView.as_view(), name="teacher_detail"),

    path("studentCreateList/", views.StudentListCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name="student_detail"),

    path("courseCreateList/", views.CourseListCreateView.as_view(), name="course_create"),
    path("course/<int:pk>/", views.CourseRetrieveUpdateDestroyView.as_view(), name="course_detail"),

    path("sectionCreateList/", views.SectionListCreateView.as_view(), name="section_create"),
    path("section/<int:pk>/", views.SectionRetrieveUpdateDestroyView.as_view(), name="section_detail"),

    path("chapterCreateList/", views.ChapterListCreateView.as_view(), name="chapter_create"),
    path("chapter/<int:pk>/", views.ChapterRetrieveUpdateDestroyView.as_view(), name="chapter_detail"),
]