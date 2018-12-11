
from django.db import models

# Create your models here.
class userInf(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    isOnline = models.BooleanField(default=False)

  #
  # python manage.py makemigrations
  #   python manage.py migrate
