from django.db import models

# Create your models here.
class StudentModel(models.Model):
    studentName = models.CharField(max_length=100)
    studentId = models.IntegerField()
    group = models.CharField(max_length=100)
    def __str__(self):
        return self.studentName