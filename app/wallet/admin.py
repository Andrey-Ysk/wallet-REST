from django.contrib import admin
from .models import Wallets, Transactions


admin.site.register(Wallets)
admin.site.register(Transactions)