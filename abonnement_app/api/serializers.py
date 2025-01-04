from rest_framework import serializers
from abonnement_app.models import Subscription, Payment
from user_app.api.serializers import UserSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__' 
        #fields = ["id", "subscription", "stripe_charge_id", "amount", "timestamp"]

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__' 
        #fields = ["id", "user", "stripe_customer_id", "stripe_subscription_id", "plan", "is_active", "payments"]