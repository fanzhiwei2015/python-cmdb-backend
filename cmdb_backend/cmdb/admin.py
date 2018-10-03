from django.contrib import admin

# Register your models here.
from .models import Bu, Product, Application

admin.site.register(Bu)
admin.site.register(Product)
admin.site.register(Application)