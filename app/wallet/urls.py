from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers
from .views import WalletsViewSet, TransactionsViewSet, AllTransactionsViewSet


wallets_router = routers.DefaultRouter()
wallets_router.register(r'wallets', WalletsViewSet, basename='wallets')
wallets_router.register(r'transactions', AllTransactionsViewSet)

transaction_router = routers.NestedDefaultRouter(wallets_router, r'wallets', lookup='wallets')
transaction_router.register(r'transactions', TransactionsViewSet, basename='transactions')

urlpatterns = [
    url(r'^api/', include(wallets_router.urls)),
    url(r'^api/', include(transaction_router.urls)),
]