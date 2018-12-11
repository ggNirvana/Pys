from django.db import models

# Create your models here.

class mainInf(models.Model):
    longi = models.CharField(max_length=20)
    lati = models.CharField(max_length=20)
    username = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)

