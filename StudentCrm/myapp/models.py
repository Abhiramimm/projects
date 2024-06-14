from django.db import models

# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=200)

    course=models.CharField(max_length=200)

    batch=models.PositiveIntegerField()

    duration=models.PositiveIntegerField()

    phone_no=models.PositiveIntegerField()


    def __str__(self):

        return self.name 


