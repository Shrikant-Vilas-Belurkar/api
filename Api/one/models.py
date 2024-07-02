from django.db import models

# Create your models here.
class Api(models.Model):
    fname = models.CharField(max_length=100)
    fstart = models.CharField(max_length=100)
    fend = models.CharField(max_length=100)
    fdate = models.DateField()
    ffare = models.FloatField()

