from django.db import models


# Create your models here.
class user_details(models.Model):
    fullname = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=16, blank=False, null=False)
    gender_choice = [('M', 'Male'), ('F', 'FeMale')]
    gender = models.CharField(choices=gender_choice)
    birthdate = models.DateField()
    city = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now=True)
