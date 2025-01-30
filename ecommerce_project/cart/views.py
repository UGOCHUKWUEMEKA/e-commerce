from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cart
from .serializers import CartSerializer
from rest_framework import status
from products.models import Product

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Only show items in the cart for the authenticated user
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    # Custom action to add a product to the cart
    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the product is already in the cart
        cart_item, created = Cart.objects.get_or_create(
            user=request.user, product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            # If already in cart, update quantity
            cart_item.quantity += quantity
            cart_item.save()

        return Response(CartSerializer(cart_item).data, status=status.HTTP_201_CREATED)

    # Custom action to update the quantity of a product in the cart
    @action(detail=True, methods=['put'])
    def update_quantity(self, request, pk=None):
        cart_item = self.get_object()
        new_quantity = request.data.get('quantity')

        if new_quantity is None or new_quantity <= 0:
            return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item.quantity = new_quantity
        cart_item.save()

        return Response(CartSerializer(cart_item).data)

    # Custom action to remove an item from the cart
    @action(detail=True, methods=['delete'])
    def remove_from_cart(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.delete()
        return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)
