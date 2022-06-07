from operator import mod
from django.db import models

class Session(models.Model):
    tutor = models.ForeignKey("tutor", on_delete=models.CASCADE)
    parent = models.ForeignKey("parent", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    skill_level = models.CharField(max_length=25)