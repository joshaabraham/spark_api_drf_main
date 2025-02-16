from django.urls import path
from . import views



urlpatterns = [
    path('job-opportunities/', views.JobOpportunityListCreateView.as_view(), name='job-opportunity-list-create'),
    path('job-opportunities/<int:pk>/', views.JobOpportunityDetailView.as_view(), name='job-opportunity-detail'),
    path('required-skills/', views.RequiredSkillListCreateView.as_view(), name='required-skill-list-create'),
    path('required-skills/<int:pk>/', views.RequiredSkillDetailView.as_view(), name='required-skill-detail'),
    path('required-languages/', views.RequiredLanguageListCreateView.as_view(), name='required-language-list-create'),
    path('required-languages/<int:pk>/', views.RequiredLanguageDetailView.as_view(), name='required-language-detail'),
    path('job-applications/', views.JobApplicationListCreateView.as_view(), name='job-application-list-create'),
    path('job-applications/<int:pk>/', views.JobApplicationDetailView.as_view(), name='job-application-detail'),
]