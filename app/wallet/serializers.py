from rest_framework import serializers
from .models import Wallets, Transactions


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'