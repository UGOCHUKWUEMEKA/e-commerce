from django.contrib import admin
from .models import Category, Product, Review, Discount

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    search_fields = ('name',)
    list_filter = ('parent_category',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vendor', 'category', 'stock_quantity', 'created_date')
    search_fields = ('name', 'vendor__name', 'category__name')
    list_filter = ('vendor', 'category', 'created_date')
    prepopulated_fields = {'name': ('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('rating', 'created_at')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount_percentage', 'start_date', 'end_date')
    search_fields = ('product__name',)
    list_filter = ('start_date', 'end_date')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Discount, DiscountAdmin)
