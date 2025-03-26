from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
import stripe
from abonnement_app.models import Subscription, Payment, Payout, Transfer
from abonnement_app.api.serializers import SubscriptionSerializer, PaymentSerializer, PayoutSerializer, TransferSerializer

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

class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        subscription_id = request.data.get('subscription_id')
        amount = request.data.get('amount')

        try:
            subscription = Subscription.objects.get(id=subscription_id)
            payment = create_payment(subscription, amount)
            return Response({"message": "Payment successful", "payment": PaymentSerializer(payment).data}, status=status.HTTP_201_CREATED)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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

class CreatePayoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        amount = request.data.get('amount')

        try:
            payout = create_payout(user, amount)
            return Response({"message": "Payout successful", "payout": PayoutSerializer(payout).data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def create_payout(user, amount):
    payout = stripe.Payout.create(
        amount=int(amount * 100),  # Stripe payout en centimes
        currency="usd",
        method="instant",
        destination=user.stripe_account_id,
    )

    payout_record = Payout.objects.create(
        user=user,
        stripe_payout_id=payout["id"],
        amount=amount,
    )

    return payout_record

class CreateTransferView(APIView):
    def post(self, request, *args, **kwargs):
        source_user = request.user
        destination_user_id = request.data.get('destination_user_id')
        amount = request.data.get('amount')
        commission = request.data.get('commission')

        try:
            destination_user = settings.AUTH_USER_MODEL.objects.get(id=destination_user_id)
            transfer = create_transfer(source_user, destination_user, amount, commission)
            return Response({"message": "Transfer successful", "transfer": TransferSerializer(transfer).data}, status=status.HTTP_201_CREATED)
        except settings.AUTH_USER_MODEL.DoesNotExist:
            return Response({"error": "Destination user not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def create_transfer(source_user, destination_user, amount, commission):
    transfer = stripe.Transfer.create(
        amount=int(amount * 100),  # Stripe transfer en centimes
        currency="usd",
        destination=destination_user.stripe_account_id,
    )

    transfer_record = Transfer.objects.create(
        source_user=source_user,
        destination_user=destination_user,
        stripe_transfer_id=transfer["id"],
        amount=amount,
        commission=commission,
    )

    return transfer_record

class ProcessAutomaticPaymentsView(APIView):
    def post(self, request, *args, **kwargs):
        process_automatic_payments()
        return Response({"message": "Automatic payments processed"}, status=status.HTTP_200_OK)

def process_automatic_payments():
    active_subscriptions = Subscription.objects.filter(is_active=True)
    for subscription in active_subscriptions:
        amount = get_subscription_amount(subscription.plan)
        create_payment(subscription, amount)

def get_subscription_amount(plan):
    # Define plan amounts here, example:
    if plan == "basic":
        return 9.99
    elif plan == "pro":
        return 19.99
    elif plan == "enterprise":
        return 49.99
    else:
        return 0
