from django.db import models

class Review(models.Model):
    tutor_review = models.CharField(max_length=1000)
    parent = models.ForeignKey("parent", on_delete=models.CASCADE)
    tutor = models.ForeignKey("tutor", on_delete=models.CASCADE)