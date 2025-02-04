from rest_framework import serializers
from .models import Wishlist
from products.serializers import ProductSerializer
from accounts.serializers import AccountSerializer


class WishlistSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ["user", "product"]
