from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from config.routers import *
from .routers import shop_router
from .serializers import *
from .views import *
import config.urls


urlpatterns = shop_router.urls
