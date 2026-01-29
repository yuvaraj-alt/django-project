from django.db import models

# Create your models here.

class BookModel(models.Model):
    bookName = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    pickupDate = models.DateField()
    receivedDate = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100,choices=[("reading","Reading"),("completed","Completed"),("on hold","On Hold")])

    def __str__(self):
        return self.bookName
