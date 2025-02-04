from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order, OrderItem, Payment
from .serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter orders by the authenticated user
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the currently authenticated user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["put"])
    def update_status(self, request, pk=None):
        order = self.get_object()
        status = request.data.get("status")

        if status not in dict(Order.STATUS_CHOICES):
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )

        order.status = status
        order.save()
        return Response(OrderSerializer(order).data)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter order items by the authenticated user's orders
        order = self.kwargs["order_pk"]
        return OrderItem.objects.filter(order__id=order)

    def perform_create(self, serializer):
        order = Order.objects.get(id=self.kwargs["order_pk"])
        serializer.save(order=order)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter payments by the authenticated user's orders
        return Payment.objects.filter(order__user=self.request.user)

    def perform_create(self, serializer):
        order = Order.objects.get(id=self.kwargs["order_pk"])
        serializer.save(order=order)

    @action(detail=True, methods=["put"])
    def update_payment_status(self, request, pk=None):
        payment = self.get_object()
        payment_status = request.data.get("payment_status")

        if payment_status not in dict(Payment.PAYMENT_STATUS_CHOICES):
            return Response(
                {"error": "Invalid payment status"}, status=status.HTTP_400_BAD_REQUEST
            )

        payment.payment_status = payment_status
        payment.save()
        return Response(PaymentSerializer(payment).data)
