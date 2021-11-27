from django.contrib import admin
from django.urls import path, include
from config.routers import *
from .serializers import *
from .views import *
import config.urls


urlpatterns = [
    path('data/', include(user_router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', RegisterView.as_view(), name='register')
]
