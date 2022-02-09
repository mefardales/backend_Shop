from django.db import models
import uuid

# Create your models here.
class Menu(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1())
    date_menu = models.DateField(null=False)

class MenuOptions(models.Model):
    menu = models.ForeignKey(
        "Menu", on_delete=models.CASCADE, null=False)
    option = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
