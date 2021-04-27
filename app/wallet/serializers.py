from django.db.models import Sum
from rest_framework import serializers
from .models import Wallets, Transactions


class WalletSerializer(serializers.ModelSerializer):
    wallet_total = serializers.SerializerMethodField()
    class Meta:
        model = Wallets
        fields = '__all__'

    def get_wallet_total(self, obj):
        wallettotal = Transactions.objects.filter(wallet=obj).aggregate(wallet_total=Sum('amount'))
        return wallettotal['wallet_total']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
