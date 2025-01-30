# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Wishlist
from .serializers import WishlistSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access these views

    def get_queryset(self):
        """
        Limit the queryset to only the wishlist items belonging to the authenticated user.
        """
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user to the wishlist item when it is created.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def view_wishlist(self, request):
        """
        View the products in the user's wishlist.
        """
        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def remove_from_wishlist(self, request, pk=None):
        """
        Remove a specific product from the user's wishlist.
        """
        wishlist_item = self.get_object()
        if wishlist_item.user == request.user:
            wishlist_item.delete()
            return Response({'message': 'Product removed from wishlist'}, status=204)
        return Response({'message': 'You cannot remove products from other users\' wishlist'}, status=403)
