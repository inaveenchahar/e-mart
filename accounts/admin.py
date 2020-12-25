from django.contrib import admin
from .models import UserAddress

# Register your models here.


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone_no', 'pincode', 'added_on', 'updated_on']


admin.site.register(UserAddress, UserAddressAdmin)
