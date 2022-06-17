from operator import mod
from django.db import models
from bridgethegapapi.models import language
from bridgethegapapi.models.parent import Parent

class Session(models.Model):
    tutor = models.ForeignKey("tutor", on_delete=models.CASCADE)
    parents = models.ManyToManyField("Parent", related_name="parents")
    date = models.DateField()
    time = models.TimeField()
    skill_level = models.CharField(max_length=25)
    language = models.ManyToManyField("Language", related_name="languages", through="SessionLanguage")
    
    @property
    def joined(self):
        return self.__joined
    
    @joined.setter
    def joined(self, value):
        self.__joined = value
        
    # has th parent user joined this tutoring session, each instance of this session, did the parent join
    # add custom property to Session model class.