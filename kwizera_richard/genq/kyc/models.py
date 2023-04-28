from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    date_of_birth = models.DateTimeField(max_length=23)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    town = models.CharField(max_length=10)
    zip_code = models.IntegerField(max_length=10)
    phone = models.IntegerField(max_length=10)
    phone2 = models.IntegerField(max_length=10)
    email = models.CharField(max_length=30)

