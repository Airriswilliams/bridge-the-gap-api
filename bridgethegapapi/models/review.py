from django.db import models

class Review(models.Model):
    session_review = models.CharField(max_length=1000)
    parent = models.ForeignKey("parent", on_delete=models.CASCADE)
    session = models.ForeignKey("session", on_delete=models.CASCADE)
    tutor = models.ForeignKey("tutor", on_delete=models.CASCADE)