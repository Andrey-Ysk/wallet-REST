from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Wallets, Transactions
from .serializers import WalletSerializer, TransactionSerializer


class WalletsViewSet(viewsets.ModelViewSet):
    queryset = Wallets.objects.all()
    serializer_class = WalletSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()

    def get_queryset(self):
        return Transactions.objects.filter(wallet=self.kwargs['wallets_pk'])

    serializer_class = TransactionSerializer


class AllTransactionsViewSet(ListModelMixin, GenericViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
