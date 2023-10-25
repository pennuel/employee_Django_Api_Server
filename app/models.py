from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)
