# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access these views

    def get_queryset(self):
        """
        Limit the queryset to only the vendor belonging to the authenticated user.
        """
        return Vendor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user to the vendor profile when a new vendor is created.
        """
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        """
        Custom action to retrieve the profile of a specific vendor.
        """
        vendor = self.get_object()
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_profile(self, request, pk=None):
        """
        Custom action to update the vendor's profile information.
        """
        vendor = self.get_object()
        serializer = VendorSerializer(vendor, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
