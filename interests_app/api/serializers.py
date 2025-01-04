from rest_framework import serializers
from interests_app.models import UserInterest, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class UserInterestSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(many=False)

    class Meta:
        model = UserInterest
        fields = '__all__'

    def create(self, validated_data):
        interest_data = validated_data.pop('interest')
        interest, _ = Interest.objects.get_or_create(name=interest_data['name'])
        user_interest = UserInterest.objects.create(interest=interest, **validated_data)
        return user_interest