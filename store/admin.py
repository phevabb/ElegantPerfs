from django.contrib import admin
from .models import Product, Variation
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
     
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.images.url))
    
    list_display = ('product_name', 'price', 'old_price', 'category',  'is_available', 'stock', 'image_tag',)
    list_editable = ('price', 'old_price', 'stock')
    prepopulated_fields = {'slug': ('product_name',)}



class VariationAdmin(admin.ModelAdmin):
    list_display =('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ( 'is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)