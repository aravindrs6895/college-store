from django.db import models


# Create your models here.
class bio(models.Model):
    name = models.CharField(max_length=40)
    DOB = models.DateField()
    Age = models.IntegerField()
    Gender = models.TextField()
    Phone = models.IntegerField()
    Email = models.TextField()
    Address = models.TextField()
    Department = models.TextField()
    Material = models.TextField()
