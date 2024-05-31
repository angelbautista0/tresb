from rest_framework import serializers
from .models import Product, Inventories, Orders

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','sku','created_at')
        read_only_fields = ('created_at', )

class InventoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventories
        fields = ('id','sku','inventario','umbral','created_at')
        read_only_fields = ('created_at', )

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','sku','cantidad','created_at')
        read_only_fields = ('created_at', )