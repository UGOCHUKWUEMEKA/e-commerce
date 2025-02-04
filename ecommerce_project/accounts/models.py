from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone


class Account(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(
        max_length=64, unique=True, blank=True, null=True, db_index=True
    )
    verification_token_created_at = models.DateTimeField(auto_now_add=True)

    def generate_verification_token(self):
        self.verification_token = get_random_string(64)
        self.verification_token_created_at = timezone.now()
        self.save(update_fields=["verification_token", "verification_token_created_at"])

    def save(self, *args, **kwargs):
        if not self.verification_token:
            self.generate_verification_token()
        super().save(*args, **kwargs)


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="shipping_addresses"
    )
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s Address"


class Notification(models.Model):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"


from django.conf import settings
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class CustomToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)

    def save_tokens(self, user):
        # Generate new tokens for the user
        refresh = RefreshToken.for_user(user)
        self.refresh_token = str(refresh)
        self.access_token = str(refresh.access_token)
        self.save()

    def __str__(self):
        return f"Tokens for {self.user.username}"
