from django.db import models

# Create your models here.

class Sample(models.Model):
    S_No =  models.CharField(max_length=255)
    PId =  models.CharField(max_length=255)
    PName =  models.CharField(max_length=255)  
    City =  models.CharField(max_length=255)
    Hospital_Name =  models.CharField(max_length=255)
    Gender =  models.CharField(max_length=255)
    BMI =  models.CharField(max_length=255)
    DOB =  models.CharField(max_length=255)
    Hieght =  models.CharField(max_length=255)
    Weight =  models.CharField(max_length=255)
    Diabetic =  models.CharField(max_length=255)    

    def __str__(self):
        return self.S_No