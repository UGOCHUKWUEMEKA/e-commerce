from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'contact_email', 'phone_number', 'city', 'country', 'created_at', 'updated_at')
    list_filter = ('country', 'state', 'city')
    search_fields = ('company_name', 'user__email', 'contact_email', 'phone_number')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'company_name', 'description', 'contact_email', 'phone_number', 'website_url')
        }),
        ('Address Information', {
            'fields': ('address', 'country', 'state', 'city', 'zip_code')
        }),
        ('Timestamps', {
            'fields': (),  # Remove 'created_at' and 'updated_at'
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')  # Ensure they are displayed as read-only

admin.site.register(Vendor, VendorAdmin)
