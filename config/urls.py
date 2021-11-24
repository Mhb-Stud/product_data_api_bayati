"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gateway.views import Handler
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('', Handler, basename='create')
router.register('auth/', Handler, include('dj_rest_auth.urls'))
urlpatterns = router.urls


# these are two endpoints to access the api
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('get/', TestView.as_view()),
#     path('post/', TestView.as_view()),
# ]
