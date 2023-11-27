from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.IntegerField(max_length=10,null=True)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50,null=True)
    branch = models.CharField(max_length=50,null=True)
    account_type = models.CharField(max_length=50)
    materials_provide = models.CharField(max_length=100)



