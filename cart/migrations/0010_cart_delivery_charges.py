# Generated by Django 3.1.1 on 2020-12-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cart_ordered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivery_charges',
            field=models.IntegerField(default=40),
        ),
    ]
