# Generated by Django 3.1.1 on 2020-12-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, help_text='Display order', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.IntegerField(blank=True, help_text='Display order', null=True),
        ),
    ]
