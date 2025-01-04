from django.urls import path
from . import views

urlpatterns = [
    path("job_offersCreateList/", views.JobOfferListCreateView.as_view(), name="job_offer_list_create"),
    path("job_offer/<int:pk>/", views.JobOfferRetrieveUpdateDestroyView.as_view(), name="job_offer_detail"),

    path("job_searchesCreateList/", views.JobSearchListCreateView.as_view(), name="job_search_list_create"),
    path("job_search/<int:pk>/", views.JobSearchRetrieveUpdateDestroyView.as_view(), name="job_search_detail"),
]