from gateway.views import *
from user.views import *
from rest_framework.routers import DefaultRouter


# this router is responsible for sending api/ path information to CrawlerHandler Class
crawl_router = DefaultRouter()
crawl_router.register('', CrawlerHandler, basename='create')
