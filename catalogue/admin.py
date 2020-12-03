from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_price')
    search_fields = ('name',)
    list_filter = ('category__name',)

    def display_price(self, obj):
        return f'PKR {obj.price}'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
