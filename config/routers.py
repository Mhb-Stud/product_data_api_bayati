from gateway.views import Handler
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', Handler, basename='create')
