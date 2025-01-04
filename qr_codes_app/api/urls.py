from django.urls import path
from . import views

urlpatterns = [
    path("qr_codes/", views.QRCodeListCreateView.as_view(), name="qr_code_list_create"),
    path("qr_codes/<int:pk>/", views.QRCodeRetrieveUpdateDestroyView.as_view(), name="qr_code_detail"),
    path("qr_codes/<int:pk>/image/", views.QRCodeImageView.as_view(), name="qr_code_image"),
]