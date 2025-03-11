from django.urls import path
from .views import (
    SubscriptionListCreateView, SubscriptionRetrieveUpdateDestroyView,
    PaymentListCreateView, PaymentRetrieveUpdateDestroyView, CreatePaymentView,
    CreatePayoutView, CreateTransferView, ProcessAutomaticPaymentsView
)

urlpatterns = [
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateDestroyView.as_view(), name='subscription-detail'),
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
    path('create-payment/', CreatePaymentView.as_view(), name='create-payment'),
    path('create-payout/', CreatePayoutView.as_view(), name='create-payout'),
    path('create-transfer/', CreateTransferView.as_view(), name='create-transfer'),
    path('process-automatic-payments/', ProcessAutomaticPaymentsView.as_view(), name='process-automatic-payments'),
]