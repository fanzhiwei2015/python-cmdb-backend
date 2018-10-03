from django.contrib import admin

# Register your models here.
from .models import Bu, Product, Application, Host


class BuAdmin(admin.ModelAdmin):
    model = Bu
    list_display = ['name', 'owner', 'description' ]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'owner', 'description']


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['name', 'owner', 'description' ]


class HostAdmin(admin.ModelAdmin):
    model = Host
    list_display = ['name', 'ip', 'owner', 'description' ]


admin.site.register(Bu, BuAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Host, HostAdmin)