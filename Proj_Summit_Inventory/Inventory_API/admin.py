from django.contrib import admin
from TokenCreator.models import TokenManagement
from Inventory_API.models import Product

# Register your models here.
admin.site.register(TokenManagement)
admin.site.register(Product)