from rest_framework import serializers
from .models import UserProfile, PortfolioModel, CurrentMarketModel, InvestmentModel, ResourcesModel, MembershipModel, TransactionlogModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','Fname','Lname']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
            Fname=validated_data['Fname'],
            Lname=validated_data['Lname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PortfolioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModel
        fields = '__all__'

class CurrentMarketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMarketModel
        fields = '__all__'

class InvestmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentModel
        fields = '__all__'

class ResourcesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcesModel
        fields = '__all__'

class MembershipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipModel
        fields = '__all__'

class TransactionlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionlogModel
        fields = '__all__'
