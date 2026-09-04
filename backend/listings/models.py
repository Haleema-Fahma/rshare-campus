from django.conf import settings
from django.db import models


class Listing(models.Model):

    TYPE_CHOICES = [
        ("resource", "Resource"),
        ("skill", "Skill"),
    ]

    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("books", "Books"),
        ("technology", "Technology"),
        ("electronics", "Electronics"),
        ("photography", "Photography"),
        ("programming", "Programming"),
        ("design", "Design"),
        ("sports", "Sports"),
        ("other", "Other"),
    ]

    CONDITION_CHOICES = [
        ("new", "New"),
        ("excellent", "Excellent"),
        ("good", "Good"),
        ("fair", "Fair"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="listings"
    )

    listing_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to="listings/",
        blank=True,
        null=True
    )

    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        blank=True
    )

    credit_cost = models.PositiveIntegerField(
        default=10
    )

    duration_days = models.PositiveIntegerField(
        default=7
    )

    location = models.CharField(
        max_length=150,
        default="RCSS Campus"
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title