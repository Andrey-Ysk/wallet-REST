from django.db import models
from datetime import datetime
import uuid


class Wallets(models.Model):
    name = models.CharField(max_length=256)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallets, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField()