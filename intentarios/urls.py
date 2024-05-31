from rest_framework import routers
from .api import ProductViewSet, InventoriesViewSet, OrdersViewSet 

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')
router.register('api/inventories/product', InventoriesViewSet, 'inventories')
router.register('api/orders', OrdersViewSet, 'orders')

urlpatterns = router.urls