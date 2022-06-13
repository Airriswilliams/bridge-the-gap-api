from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100) 
    schedule = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='tutors', height_field=None, 
                                    width_field=None, null=True, blank=True)