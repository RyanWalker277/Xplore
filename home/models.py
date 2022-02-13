from email.policy import default
from django.db import models

# Create your models here.

class Data(models.Model):
    college_name = models.CharField(max_length=500)
    img = models.URLField(max_length = 5000 , null=True , default = 0)
    desc = models.CharField(max_length=200 , default = 0 , null=True)

    def __str__(self):
        return self.college_name

class StudentData(models.Model):
    First_Name = models.CharField(max_length=500)
    Last_Name = models.CharField(max_length = 500 , null=True)
    Email = models.CharField(max_length = 5000 , null=True)
    Class_10_marks = models.IntegerField(null=True)
    Class_12_marks = models.IntegerField(null=True)

    
