from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "created_at",
    )  # Add any fields you want to display
    search_fields = ("user__username", "product__name")  # Search by user and product
    list_filter = ("user", "product")  # Filter by user and product
    ordering = ("-created_at",)  # Default ordering (optional)


admin.site.register(Wishlist, WishlistAdmin)
