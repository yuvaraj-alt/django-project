from django.db import models

# Create your models here.
class TicketBooking(models.Model):
    passengerName = models.CharField(max_length=100)
    classType = models.CharField(max_length=100)
    IdProof = models.CharField(max_length=100)
    startStation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    Date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.passengerName