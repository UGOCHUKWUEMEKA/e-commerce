from rest_framework import serializers
from .models import Category, Product, Review, Discount
from vendors.models import Vendor
from accounts.models import Account


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent_category", "subcategories"]


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), allow_null=True
    )
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    discounts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "vendor",
            "stock_quantity",
            "category",
            "image_url",
            "created_date",
            "reviews",
            "discounts",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = ["id", "user", "product", "rating", "comment", "created_at"]


class DiscountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Discount
        fields = ["id", "product", "discount_percentage", "start_date", "end_date"]
