from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Added by')
    full_name = models.CharField(max_length=50, help_text='Full Name of the user')
    phone_no = models.CharField(max_length=10, help_text='Phone Number')
    pincode = models.CharField(max_length=6, help_text='Address Pincode')
    house_no = models.CharField(max_length=30, help_text='House/Flat no. and building name',)
    address = models.CharField(max_length=50, help_text='Area, Colony, Street, Sector, Village')
    landmark = models.CharField(max_length=30, blank=True, help_text='Landmark e.g. Paras Hospital, DPS School')
    city = models.CharField(max_length=30)
    default_address = models.BooleanField(default=False, help_text='Mark this for future items to be delivered at this address')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.full_name)

    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
