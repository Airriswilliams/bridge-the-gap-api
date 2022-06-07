from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100) 
    schedule = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)