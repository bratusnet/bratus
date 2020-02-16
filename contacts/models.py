from django.db import models
from datetime import datetime

class Contact(models.Model):

    name=models.CharField (max_length=200, blank=True)
    jtype=models.CharField (max_length=100, blank=True)
    joke=models.TextField (default=0)
    contact_date=models.DateTimeField  (blank=True,default=datetime.now)
    user_id=models.IntegerField (blank=True)
    rating=models.IntegerField (default=0, blank=True)
    def __str__ (self):
        return self.name

