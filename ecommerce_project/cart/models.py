from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="cart"
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart"
