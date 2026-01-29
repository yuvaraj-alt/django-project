from django.db import models

# Create your models here.

class QuizModel(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)

    def __str__(self):
        return self.option1




