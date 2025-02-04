from rest_framework import serializers
from .models import Vendor
from accounts.models import Account


class VendorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())

    class Meta:
        model = Vendor
        fields = [
            "id",
            "user",
            "company_name",
            "description",
            "contact_email",
            "phone_number",
            "website_url",
            "address",
            "country",
            "state",
            "city",
            "zip_code",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
