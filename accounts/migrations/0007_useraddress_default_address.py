# Generated by Django 3.1.1 on 2020-12-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_useraddress_default_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]
