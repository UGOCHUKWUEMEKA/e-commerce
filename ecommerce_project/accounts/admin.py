from django.contrib import admin
from .models import Account, ShippingAddress, Notification

class ShippingAddressInline(admin.TabularInline):
    model = ShippingAddress
    extra = 1

class NotificationInline(admin.TabularInline):
    model = Notification
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'profile_picture', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    inlines = [ShippingAddressInline, NotificationInline]

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line1', 'city', 'state', 'country', 'postal_code', 'phone_number')
    search_fields = ('user__username', 'city', 'state', 'country')
    list_filter = ('state', 'country')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'created_at')
