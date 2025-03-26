from rest_framework import serializers
from abonnement_app.models import Subscription, Payment, Payout, Transfer
from user_app.api.serializers import UserSerializer


class Meta:
        model = Subscription
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)