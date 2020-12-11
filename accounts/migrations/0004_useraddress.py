# Generated by Django 3.1.1 on 2020-12-09 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_delete_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
                ('house_no', models.CharField(help_text='House/Flat no. and building name', max_length=30)),
                ('address', models.CharField(help_text='Area, Colony, Street, Sector, Village', max_length=50)),
                ('landmark', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]