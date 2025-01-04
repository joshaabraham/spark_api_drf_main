from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
import stripe
from abonnement_app.models import Subscription, Payment
from abonnement_app.api.serializers import SubscriptionSerializer, PaymentSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def create_payment(subscription, amount):
    charge = stripe.Charge.create(
        customer=subscription.stripe_customer_id,
        amount=int(amount * 100),  # Stripe charge en centimes
        currency="usd",
        description=f"Paiement pour l'abonnement {subscription.pk}",
    )

    payment = Payment.objects.create(
        subscription=subscription,
        stripe_charge_id=charge["id"],
        amount=amount,
    )

    send_payment_email(payment)
    return payment

def send_payment_email(payment):
    send_mail(
        "Notification de paiement",
        f"Cher utilisateur,\n\nNous avons reçu votre paiement de ${payment.amount} pour votre abonnement.\n\nMerci de votre confiance !",
        settings.DEFAULT_FROM_EMAIL,
        [payment.subscription.user.email],
        fail_silently=False,
    )

def refund_payment(payment):
    stripe.Refund.create(charge=payment.stripe_charge_id)
    payment.delete()

def cancel_payment(payment):
    payment.delete()

def process_automatic_payments():
    active_subscriptions = Subscription.objects.filter(is_active=True)
    for subscription in active_subscriptions:
        amount = get_subscription_amount(subscription.plan)
        create_payment(subscription, amount)

def get_subscription_amount(plan):
    # Définissez les montants des plans ici, exemple :
    if plan == "basic":
        return 9.99
    elif plan == "pro":
        return 19.99
    elif plan == "enterprise":
        return 49.99
    else:
        return 0
