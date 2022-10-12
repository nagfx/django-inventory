from rest_framework import serializers

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        depth = 1
        fields = '__all__'
        # fields = ('id', 'name', 'supplier')


# class SupplierSerializer(serializers.ModelSerializer):
#     inventories = InventorySerializer(source='inventory_set', many=True)

#     class Meta:
#         model = Supplier
#         fields = ("inventories", 'id', 'name')

    # '__all__'
    # fields = ("id", "name", "description", "note",
    #           "stock", "availability", "supplier")
