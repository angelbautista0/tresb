from .models import Product, Inventories, Orders
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, InventoriesSerializer, OrdersSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class InventoriesViewSet(viewsets.ModelViewSet):
    queryset = Inventories.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InventoriesSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdersSerializer