from datetime import datetime

from rest_framework import serializers
from Inventory_API.models import Product





####Try inheriet from django base user
#User (inherit from base user)
#Token #cached in db
class ProductSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()

    age = age
    class Meta:
        model = Product
        fields = "__all__"


    def get_age(self, instance):
        return datetime.now().year - 1983

    def get_weight(self, instance):
        if Product.product_name == "hat":
            return "work"
        else:
            return "retire"