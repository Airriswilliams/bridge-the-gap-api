from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    child_name = models.CharField(max_length=25)
    child_age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
