from gateway.views import *
from rest_framework.routers import DefaultRouter


crawl_router = DefaultRouter()
crawl_router.register('', CrawlerHandler, basename='create')

user_router = DefaultRouter()
user_router.register('', UserHandler, basename='review')
