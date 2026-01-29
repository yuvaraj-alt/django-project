from django.db import models

# Create your models here.

class AppointModel(models.Model):
    clientName = models.CharField(max_length=200)
    clientNum = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100,choices=[("available","Available"),("booked","Booked"),("cancelled","Cancelled")])

    def __str__(self):
        return self.clientName