from django.db import models
from datetime import date
# Create your models here.

class CustomUser(models.Model):
    fullname = models.CharField(max_length=50)
    password = models.TextField()
    phone = models.TextField()
    date = models.DateField(default=date.today) 
    token = models.TextField()
    id = models.AutoField(primary_key=True)