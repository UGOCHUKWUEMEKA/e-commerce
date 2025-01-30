from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, ShippingAddressViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'addresses', ShippingAddressViewSet, basename='shipping-address')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('api/', include(router.urls)),
]
