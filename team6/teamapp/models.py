from django.db import models

# Create your models here.

class Students (models.Model):
    roll = models.CharField(max_length=10)
    s_n = models.CharField(max_length=10)
    pic = models.ImageField()
