from django.db import models

# Create your models here.
class Position(models.Model):
    title   = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    time    = models.CharField(max_length=50)
    tech    = models.CharField(max_length=50)
    desc    = models.TextField()
    img     = models.FilePathField(path="/img")
    
