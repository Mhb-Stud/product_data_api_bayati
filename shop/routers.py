from rest_framework.routers import DefaultRouter
from .views import ShopManager

shop_router = DefaultRouter()
shop_router.register('products', ShopManager, basename='shop_manager')
