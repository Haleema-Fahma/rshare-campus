from django.conf import settings
from django.db import models


class ExchangeRequest(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    listing = models.ForeignKey(
        "listings.Listing",
        on_delete=models.CASCADE,
        related_name="requests"
    )

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exchange_requests"
    )

    message = models.TextField(
        blank=True
    )

    requested_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.requester.username} - {self.listing.title}"

class Exchange(models.Model):

    STATUS_CHOICES = [
        ("approved", "Approved"),
        ("handover", "Handover"),
        ("borrowed", "Borrowed"),
        ("returned", "Returned"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("disputed", "Disputed"),
    ]

    request = models.OneToOneField(
        ExchangeRequest,
        on_delete=models.CASCADE,
        related_name="exchange"
    )

    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrowed_exchanges"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_exchanges"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="approved"
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    handover_code = models.CharField(
        max_length=20,
        blank=True
    )

    return_code = models.CharField(
        max_length=20,
        blank=True
    )

    borrowed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    returned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    return_condition = models.CharField(
        max_length=100,
        blank=True
    )

    return_notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Exchange #{self.id}"

class ExchangeDispute(models.Model):

    STATUS_CHOICES = [
        ("open", "Open"),
        ("under_review", "Under Review"),
        ("resolved", "Resolved"),
        ("rejected", "Rejected"),
    ]

    exchange = models.ForeignKey(
        Exchange,
        on_delete=models.CASCADE,
        related_name="disputes"
    )

    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    reason = models.TextField()

    evidence = models.ImageField(
        upload_to="disputes/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    admin_notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Dispute #{self.id}"


class Rating(models.Model):

    exchange = models.ForeignKey(
        Exchange,
        on_delete=models.CASCADE,
        related_name="ratings"
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ratings_given"
    )

    reviewee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ratings_received"
    )

    rating = models.PositiveIntegerField(
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ]
    )

    comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.rating}/5 - {self.reviewer.username}"