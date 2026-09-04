from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ("student", "Student"),
        ("staff", "Staff"),
        ("admin", "Admin"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    college_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Profile(models.Model):

    YEAR_CHOICES = [
        ("1", "First Year"),
        ("2", "Second Year"),
        ("3", "Third Year"),
        ("4", "Fourth Year"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    year = models.CharField(
        max_length=10,
        choices=YEAR_CHOICES,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    eco_credits = models.PositiveIntegerField(
        default=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.db.models.signals import post_save
from django.dispatch import receiver
from credits.models import Wallet


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            eco_credits=100
        )
        Wallet.objects.create(
            user=instance,
            balance=100
        )