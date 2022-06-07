from django.db import models
# JOIN TABLE

class SessionLanguage(models.Model):
    language = models.ForeignKey("language", on_delete=models.CASCADE)
    session = models.ForeignKey("session", on_delete=models.CASCADE)