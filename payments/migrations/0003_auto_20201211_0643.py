# Generated by Django 3.1.1 on 2020-12-11 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_order_order_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='completed',
        ),
    ]
