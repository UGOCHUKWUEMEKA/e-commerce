from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"orders/(?P<order_pk>\d+)/items", OrderItemViewSet)
router.register(r"orders/(?P<order_pk>\d+)/payments", PaymentViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
