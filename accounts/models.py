from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    house_no = models.CharField(max_length=30, help_text='House/Flat no. and building name')
    address = models.CharField(max_length=50, help_text='Area, Colony, Street, Sector, Village')
    landmark = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30)
    default_address = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.full_name)

    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
