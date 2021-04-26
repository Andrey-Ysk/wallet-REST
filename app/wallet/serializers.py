from rest_framework import serializers
from .models import Wallets, Transactions


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('balance', None)
        return super().update(instance, validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'