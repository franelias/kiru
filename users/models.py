from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    type = models.BooleanField()
