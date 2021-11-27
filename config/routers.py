from gateway.views import *
from user.views import *
from rest_framework.routers import DefaultRouter


# this router is responsible for sending api/ path information to CrawlerHandler Class
crawl_router = DefaultRouter()
crawl_router.register('', CrawlerHandler, basename='create')

# this router is responsible for sending user/ path information to UserHandler Class
user_router = DefaultRouter()
user_router.register('', UserHandler, basename='review')
