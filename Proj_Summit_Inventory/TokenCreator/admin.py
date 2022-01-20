from django.contrib import admin
from TokenCreator.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'delete_now')


admin.site.register(Product, ProductAdmin)
