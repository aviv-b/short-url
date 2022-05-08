from wsgiref.validate import validator
from django.db import models

# Create your models here.

class Url(models.Model):
    """Url"""
    id = models.AutoField(primary_key=True)
    short_url = models.CharField(max_length=7,blank=True)
    long_url = models.URLField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)