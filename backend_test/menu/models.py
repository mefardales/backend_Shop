from django.db import models
import uuid

# Create your models here.
class Menu(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1())
    date_menu = models.DateField(null=False, blank=False)

class MenuOptions(models.Model):
    option = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    menu = models.ForeignKey(
       "Menu", on_delete=models.CASCADE, null=False, blank=False)
    
