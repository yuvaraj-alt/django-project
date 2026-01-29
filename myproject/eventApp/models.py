from django.db import models

# Create your models here.
class EventModel(models.Model):
    eventName = models.CharField(max_length=200)
    attendeeName = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    registrationStatus = models.CharField(max_length=100,choices=[("registered","Registered"),("not registered","Not Registered")])

    def __str__(self):
        return self.eventName