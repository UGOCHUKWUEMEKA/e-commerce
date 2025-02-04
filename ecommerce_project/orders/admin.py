from django.contrib import admin
from .models import Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display by default


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("user__username",)
    inlines = [OrderItemInline]


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "payment_method",
        "payment_status",
        "transaction_id",
        "payment_date",
    )
    list_filter = ("payment_status", "payment_method", "payment_date")
    search_fields = ("transaction_id",)


# Register the models
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
