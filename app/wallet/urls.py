from django.conf.urls import url
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers
from .views import WalletsViewSet, TransactionsViewSet, AllTransactionsViewSet
from django.views.generic import TemplateView


wallets_router = routers.DefaultRouter()
wallets_router.register(r'wallets', WalletsViewSet, basename='wallets')
wallets_router.register(r'transactions', AllTransactionsViewSet)

transaction_router = routers.NestedDefaultRouter(wallets_router, r'wallets', lookup='wallets')
transaction_router.register(r'transactions', TransactionsViewSet, basename='transactions')

urlpatterns = [
    url(r'^api/', include(wallets_router.urls)),
    url(r'^api/', include(transaction_router.urls)),
    path('openapi', get_schema_view(
        title="Wallet App",
    ), name='openapi-schema'),
    path('api-docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]