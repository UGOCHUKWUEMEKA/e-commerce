from rest_framework import serializers
from .models import Account, ShippingAddress, Notification
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account  # Ensure correct model usage
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        user.generate_verification_token()

        # Send email verification (Better in signals.py)
        verification_link = f"{settings.SITE_URL}{reverse('verify-email')}?token={user.verification_token}"
        send_mail(
            "Verify your email",
            f"Click the link to verify your email: {verification_link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
        ]


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            "id",
            "user",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "country",
            "postal_code",
            "phone_number",
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "user", "message", "is_read", "created_at"]


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_new_password(self, value):
        validate_password(value)  # Ensure password is strong
        return value
