from gateway.views import *
from user.views import *
from rest_framework.routers import DefaultRouter


# this router is responsible for sending api/auth/register information to RegisterView Class
registration_router = DefaultRouter()
registration_router.register('', RegisterView, basename='register')

photo_router = DefaultRouter()
photo_router.register('photo', PhotoUpload, basename='photo')
