from django.conf import settings
from django.db import models


class Wallet(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet"
    )

    balance = models.PositiveIntegerField(
        default=100
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.balance} EcoCredits"


class CreditTransaction(models.Model):

    TRANSACTION_TYPES = [
        ("welcome", "Welcome Bonus"),
        ("earned", "Earned"),
        ("spent", "Spent"),
        ("refund", "Refund"),
        ("penalty", "Penalty"),
        ("reward", "Reward Redemption"),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    amount = models.IntegerField()

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    description = models.CharField(
        max_length=255
    )

    exchange = models.ForeignKey(
        "exchanges.Exchange",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.amount} credits - {self.description}"