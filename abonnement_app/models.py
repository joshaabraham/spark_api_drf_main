from django.db import models
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscription")
    stripe_customer_id = models.CharField(max_length=50)
    stripe_subscription_id = models.CharField(max_length=50)
    plan = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # destinataire = 

    def __str__(self):
        return f"{self.user.username}'s subscription"

class Payment(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payment")
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="payment")
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # destinataire = 

    def __str__(self):
        return f"Payment {self.pk} for {self.subscription.user.username}"


class PaymentCard(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payment_card")
    #   facturatio_addresse = 
    # card information
    
    def __str__(self):
        return super().__str__()