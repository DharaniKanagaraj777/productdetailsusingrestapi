from rest_framework import serializers
from . models import ProductDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id','customername','productname','quantity','address']