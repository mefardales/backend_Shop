# Generated by Django 4.0.2 on 2022-02-11 20:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_menu_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('71380256-8b75-11ec-8c68-705681b4b5a7')),
        ),
    ]
