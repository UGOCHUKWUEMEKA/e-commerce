from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "get_username")
    list_filter = ("user", "product")
    search_fields = ("user__username", "product__name")

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = "Username"


admin.site.register(Cart, CartAdmin)
