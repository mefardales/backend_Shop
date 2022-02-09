from django.db import models
from user.models import User
from menu.models import MenuOptions
from datetime import datetime 
from commons.dateutils import time 

# Create your models here.
class MenuUser(models.Model):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, null=False, 
        blank=False)
    menu_option = models.ForeignKey(
        "menu.MenuOptions", on_delete=models.CASCADE, null=False,
        blank=False)
    quantity = models.IntegerField(default=1)
    especification = models.CharField(max_length=250, null=False,
        blank=False)
    order_date = models.DateField(default=time(option=0))



