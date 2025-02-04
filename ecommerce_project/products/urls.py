from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, DiscountViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"reviews", ReviewViewSet)
router.register(r"discounts", DiscountViewSet)

urlpatterns = [
    path("", include(router.urls)),  # Removed 'api/' so it works as /products/
]
