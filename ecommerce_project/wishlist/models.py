from django.db import models


class Wishlist(models.Model):
    user = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="wishlist"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="wishlisted_by"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set when the wishlist is created

    def __str__(self):
        return f"{self.user.username}'s wishlist"
