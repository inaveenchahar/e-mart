# Generated by Django 3.1.1 on 2020-12-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201204_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]