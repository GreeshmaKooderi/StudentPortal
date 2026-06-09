from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=30)
    place = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="profile_photos")
    
    uname = models.CharField(max_length=100, unique=True, null=True, blank=True)
    pwrd = models.CharField(max_length=100, null=True, blank=True)
    
    
