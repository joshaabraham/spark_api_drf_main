from django.urls import path
from . import views

urlpatterns = [
    path("subscriptionCreateList/", views.SubscriptionListCreateView.as_view(), name="subscription_create"),
    path("subscription/<int:pk>/", views.SubscriptionRetrieveUpdateDestroyView.as_view(), name="subscription_detail"),
    path("paymentCreateList/", views.PaymentListCreateView.as_view(), name="payment_create"),
    path("payment/<int:pk>/", views.PaymentRetrieveUpdateDestroyView.as_view(), name="payment_detail"),
]