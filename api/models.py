
from django.db import models

# Create your models here.


class Supplier(models.Model):
    # id by default is primary key so not stating

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    # id by default is primary key so not stating
    name = models.CharField(max_length=255)
    # Would be better to use Textfield for description I think
    description = models.CharField(max_length=600)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    # chose to cascade on delete since we cannot
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    supplier = models.ForeignKey(
        Supplier, related_name='inventory_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

        # will use mockaroo.com to generate mock data
