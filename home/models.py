from django.db import models

class Position(models.Model):
    company=models.CharField(max_length=50, default='test')
    title=models.CharField(max_length=50, default='test')
    time=models.CharField(max_length=50, default='test')
    location=models.CharField(max_length=50, default='test')
    desc=models.TextField(default='test')
    link=models.CharField(max_length=50, default='test')
    img=models.FilePathField(path="/img")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100, default='test')
    desc  = models.TextField(default='test')
    link  = models.CharField(max_length=200, default='test')
    img   = models.FilePathField(path="/img")

    def __str__(self):
        return self.title

class Education(models.Model):
    school = models.CharField(max_length=50, default='test')
    major = models.CharField(max_length=50, default='test')
    time = models.CharField(max_length=20, default='test')
    img = models.FilePathField(path='/img')

    def __str__(self):
        return self.school

class Skill(models.Model):
    title = models.CharField(max_length=20, default='test')

    def __str__(self):
        return self.title
