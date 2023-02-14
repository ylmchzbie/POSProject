from django.contrib import admin
from .models import ProductUnit
from .models import CustomerDetails
from .models import TechnicianDetails
from .models import SupplierDetails
from .models import ServiceType
from .models import salesOrder
from .models import serviceOrder
from .models import OrderItem

# Register your models here.
# http://localhost:8000/admin/ to access admin database

admin.site.site_header = 'John Car Aircon Company'
admin.site.site_title = 'John Car Aircon Company'

class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unitPrice', 'unitQuantity', 'unitType')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customerName', 'customerContact', 'customerEmail', 'customerAddress')

class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'techName', 'techPhone', 'techEmail', 'techSched')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'suppName', 'suppPhone', 'suppEmail', 'suppAddress')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'serviceChoice', 'estimatedCost')

class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'dateOrdered', 'products', 'totalPrice')

class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'dateOrdered', 'service')

admin.site.register(ProductUnit, UnitAdmin)
admin.site.register(CustomerDetails, CustomerAdmin)
admin.site.register(TechnicianDetails, TechnicianAdmin)
admin.site.register(SupplierDetails, SupplierAdmin)
admin.site.register(ServiceType, ServiceAdmin)
admin.site.register(salesOrder)
admin.site.register(serviceOrder)
admin.site.register(OrderItem)