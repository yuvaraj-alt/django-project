from django.db import models

class ProductModel(models.Model):
    ProductName = models.CharField(max_length=200)
    ModelName = models.CharField(max_length=200)
    ProductPrize = models.IntegerField()
    Processor = models.CharField(max_length=100)
    DeliveryDate = models.DateField(null=True,blank=True)

    def __self__(self):
        return self.ProductName

