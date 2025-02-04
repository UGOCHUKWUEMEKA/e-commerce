from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Review, Discount
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    DiscountSerializer,
)


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # You can modify permissions as needed


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # You can modify permissions as needed

    def get_queryset(self):
        """
        Optionally filter products by category or vendor.
        """
        queryset = Product.objects.all()
        category = self.request.query_params.get("category")
        vendor = self.request.query_params.get("vendor")

        if category:
            queryset = queryset.filter(category__id=category)
        if vendor:
            queryset = queryset.filter(vendor__id=vendor)

        return queryset


# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # You can modify permissions as needed

    def get_queryset(self):
        """
        Optionally filter reviews by product.
        """
        queryset = Review.objects.all()
        product = self.request.query_params.get("product")

        if product:
            queryset = queryset.filter(product__id=product)

        return queryset


# Discount ViewSet
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated]  # You can modify permissions as needed

    def get_queryset(self):
        """
        Optionally filter discounts by product.
        """
        queryset = Discount.objects.all()
        product = self.request.query_params.get("product")

        if product:
            queryset = queryset.filter(product__id=product)

        return queryset
