# Generated by Django 3.1.1 on 2020-12-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201206_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(help_text='Display order', null=True),
        ),
    ]