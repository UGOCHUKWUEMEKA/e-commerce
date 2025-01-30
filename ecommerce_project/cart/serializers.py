from rest_framework import serializers
from .models import Cart
from accounts.models import Account
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']
