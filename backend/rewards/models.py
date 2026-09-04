from django.conf import settings
from django.db import models


class Reward(models.Model):

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="rewards/",
        blank=True,
        null=True
    )

    credit_cost = models.PositiveIntegerField()

    is_active = models.BooleanField(
        default=True
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class RewardRedemption(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("redeemed", "Redeemed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reward_redemptions"
    )

    reward = models.ForeignKey(
        Reward,
        on_delete=models.CASCADE,
        related_name="redemptions"
    )

    redemption_code = models.CharField(
        max_length=50,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    redeemed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.reward.title}"