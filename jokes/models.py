from django.db import models
from datetime import datetime

class Joke(models.Model):

    name=models.CharField(max_length=200, blank=True)
    jtype=models.CharField(max_length=100)
    joke=models.TextField ()
    contact_date=models.DateTimeField (default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True)
    rating=models.IntegerField(blank=True)
    def __str__ (self):
        return self.name