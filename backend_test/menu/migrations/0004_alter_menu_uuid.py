# Generated by Django 4.0.2 on 2022-02-11 05:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8893b78e-8afc-11ec-bf53-705681b4b5a7')),
        ),
    ]
