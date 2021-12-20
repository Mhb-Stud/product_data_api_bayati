from gateway.views import *
from user.views import *
from rest_framework.routers import DefaultRouter


product_router = DefaultRouter()
product_router.register('products', UserProductView, basename='review')


# this router is responsible for sending api/auth/register information to RegisterView Class
registration_router = DefaultRouter()
registration_router.register('auth/registration', RegisterView, basename='register')

photo_router = DefaultRouter()
photo_router.register('photo', PhotoUpload, basename='photo')
