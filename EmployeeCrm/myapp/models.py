from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    location=models.CharField(max_length=200)

    email=models.EmailField()

    address=models.CharField(max_length=200)

    dateofjoin=models.DateField(null=True)

    def __str__(self):
        
        return self.name
