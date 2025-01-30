from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ShippingAddress, Notification
from .serializers import ShippingAddressSerializer, NotificationSerializer
from django.contrib.auth import get_user_model

# Account ViewSet (for user data)
class AccountViewSet(viewsets.ViewSet):
    def list(self, request):
        user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'bio': request.user.bio,
            'profile_picture': request.user.profile_picture.url if request.user.profile_picture else None,
        }
        return Response(user_data)

# Shipping Address ViewSet
class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)

# Notification ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    # Custom action for marking notification as read
    @action(detail=True, methods=['put'])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"status": "success", "message": "Notification marked as read"})
