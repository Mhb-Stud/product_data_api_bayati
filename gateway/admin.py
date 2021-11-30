from django.contrib import admin
from shop.models import Product

# added person model to admin panel for manual object creation but
# disabled admin panel since this is an api
admin.site.register(Product)
