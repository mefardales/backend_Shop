# Generated by Django 4.0.2 on 2022-02-11 21:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_alter_menu_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a7ee7a7e-8b83-11ec-933e-705681b4b5a7')),
        ),
    ]
