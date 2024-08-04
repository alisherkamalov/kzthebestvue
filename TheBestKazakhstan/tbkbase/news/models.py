from django.db import models
from datetime import date

class ItemNews(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    date = models.DateField(default=date.today) 
