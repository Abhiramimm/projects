from django.db import models

# Create your models here.

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    def tasks(self):

        qs=Task.objects.filter(employee_obj=self)

        return qs

    def __str__(self):

        return self.name


class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    completion_date=models.DateField()

    assigned_date=models.DateField()

    status=models.BooleanField(default=False)

    employee_obj=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):

        return self.title