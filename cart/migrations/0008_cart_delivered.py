# Generated by Django 3.1.1 on 2020-12-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cart_delivered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]