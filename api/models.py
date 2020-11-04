from django.db import models

# Create your models here.


class Task(models.Model):
    tile = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)


class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=10)
    debit = models.FloatField()
    credit = models.FloatField()
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
