from django.db import models
from phone_field import PhoneField

# Create your models here.
class Resume(models.Model):
    username = models.CharField(max_length=12)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = PhoneField()
    email = models.EmailField()
    skills = models.CharField(max_length=100)
    about_you = models.CharField(max_length=300)
    career = models.CharField(max_length=200)
    education = models.CharField(max_length=300)