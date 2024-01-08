from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'old_price', 'category',  'is_available', 'stock')
    list_editable = ('price', 'old_price', 'stock')
    prepopulated_fields = {'slug': ('product_name',)}

# Register your models here.
admin.site.register(Product, ProductAdmin)