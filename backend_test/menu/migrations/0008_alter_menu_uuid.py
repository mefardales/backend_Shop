# Generated by Django 4.0.2 on 2022-02-11 20:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_menu_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9495ff5a-8b75-11ec-859b-705681b4b5a7')),
        ),
    ]
