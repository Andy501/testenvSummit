from rest_framework import serializers
from TokenCreator.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class No_Delete_ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('delete_now',)
