# Generated by Django 3.1.1 on 2020-10-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Category name', max_length=30)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('order', models.IntegerField(blank=True, help_text='Display order')),
                ('visible', models.BooleanField(default=True, help_text='Visible to users')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-added_on'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Product name', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.FloatField(help_text='Product price')),
                ('order', models.IntegerField(blank=True, help_text='Display order')),
                ('visible', models.BooleanField(default=True, help_text='Visible to users')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(help_text='Product will appear in selected categories', to='products.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-added_on'],
            },
        ),
    ]
