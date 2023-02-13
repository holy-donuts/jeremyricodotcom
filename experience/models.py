from django.db import models

# Create your models here.
class position(models.Model):
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=50)
    image=models.FilePathField(path="/img")
    
