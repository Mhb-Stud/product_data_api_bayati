from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from config.routers import *
from .serializers import *
from .views import *
import config.urls


urlpatterns = [
    path('data/', include(user_router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/registration/', RegisterView.as_view(), name='register')
]
