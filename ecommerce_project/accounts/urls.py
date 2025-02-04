from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, ShippingAddressViewSet, NotificationViewSet
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"addresses", ShippingAddressViewSet, basename="shipping-address")
router.register(r"notifications", NotificationViewSet, basename="notification")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]


# accounts/urls.py
from django.urls import path
from .views import ProtectedView

urlpatterns = [
    # Add this URL pattern for the protected view
    path("protected/", ProtectedView.as_view(), name="protected_view"),
]
