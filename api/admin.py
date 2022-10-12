from django.contrib import admin
from . import models


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'availability', 'stock']
    list_editable = ['stock', 'availability']
    list_per_page: 10


# Register your models here.
admin.site.register(models.Inventory, InventoryAdmin)

# Can uncomment below if you want to access Supplier model in admin
# admin.site.register(models.Supplier)
