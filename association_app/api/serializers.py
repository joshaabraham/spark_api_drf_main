from rest_framework import serializers
from association_app.models import Member, SportEvent, Promotion, Subscription

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    sport_event = SportEventSerializer()
    promotion = PromotionSerializer()

    class Meta:
        model = Subscription
        fields = '__all__'