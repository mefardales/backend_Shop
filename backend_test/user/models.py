from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100 )
    
