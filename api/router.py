from rest_framework import routers
from .viewsets import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('order s', OrderViewSet)
router.register('order-items', OrderItemViewSet)

urlpatterns = router.urls

urlpatterns = router.urls
