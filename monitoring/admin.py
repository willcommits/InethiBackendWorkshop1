from django.contrib import admin

from .models import NetworkDevice, Service, Alert


@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):

    list_display = ('name', 'device_type', 'ip_address')


@admin.register(Service)
class NetworkDeviceAdmin(admin.ModelAdmin):

    list_display = ('name', 'url', 'service_type', 'api_location')


admin.site.register(Alert)