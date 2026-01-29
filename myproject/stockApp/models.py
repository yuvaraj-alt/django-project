from django.db import models

# Create your models here.
class StockModel(models.Model):
    supplierName = models.CharField(max_length=200)
    purchasedItem = models.CharField(max_length=200)
    manufactureDate = models.DateField()
    expiryDate = models.DateField()

    def __str__(self):
        return self.supplierName